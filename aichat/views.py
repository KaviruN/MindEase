from django.shortcuts import render, get_object_or_404, redirect
from openai import OpenAI
from dotenv import load_dotenv
from django.conf import settings
import os
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse

load_dotenv()

def filter_prompt(prompt):
    keywords_path = os.path.join(settings.BASE_DIR, 'keywords.txt')
    with open(keywords_path, 'r') as file:
        excluded_keywords = file.read()
    prompt = prompt.lower().split()
    for keyword in excluded_keywords:
        if keyword in prompt:   
          return True
    return False

   

def get_response(prompt):
    client = OpenAI(
                base_url = "https://integrate.api.nvidia.com/v1",
                api_key = os.getenv("OPENAI_API_KEY")
            )
    
    completion = client.chat.completions.create(
      model="mistralai/mistral-7b-instruct-v0.3",
      messages=[{"role":"user","content":prompt}],
      temperature=0.2,
      top_p=0.7,
      max_tokens=1024,
      stream=True
    )

    
    if filter_prompt(prompt):
      result = ""
      for chunk in completion:
          if chunk.choices[0].delta.content is not None:
              result += chunk.choices[0].delta.content

      return result
    elif not filter_prompt(prompt):
      return "Sorry, I can't help with that."
    


def chat_view(request):
    if not request.user.is_authenticated:
        return redirect('user_auth:sign_in')
    UserData.objects.get_or_create(user=request.user)
    user_data = get_object_or_404(UserData, user=request.user)
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        response = get_response(prompt)
        ChatData.objects.create(user_chat=user_data, prompt=prompt, response=response)   
    return render(request, 'chat.html')

# def sent_promt(request):
#     if not request.user.is_authenticated:
#         return redirect('user_auth:sign_in')
#     UserData.objects.get_or_create(user=request.user)
#     user_data = get_object_or_404(UserData, user=request.user)
#     if request.method == 'POST':
#         prompt = request.POST.get('prompt')
#         response = get_response(prompt)
#         ChatData.objects.create(user_chat=user_data, prompt=prompt, response=response)

def get_chat_data(request):
    if request.user.is_authenticated:
      UserData.objects.get_or_create(user=request.user)
      user_data = get_object_or_404(UserData, user=request.user)
      chat_data = user_data.user_data.all().order_by('-id').values()
      return JsonResponse({'chat_data':list(chat_data)})









