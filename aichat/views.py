from django.shortcuts import render, get_object_or_404
from openai import OpenAI
from dotenv import load_dotenv
from django.conf import settings
import os
from .models import *
from django.contrib.auth.decorators import login_required

load_dotenv()

def filter_prompt(prompt):
    keywords_path = os.path.join(settings.BASE_DIR, 'keywords.txt')
    with open(keywords_path, 'r') as file:
        excluded_keywords = file.read()
    prompt = prompt.lower().split()
    file.close()
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
    
@login_required
def chat(request):
    UserData.objects.get_or_create(user=request.user)
    user_data = get_object_or_404(UserData, user=request.user)
    chat_data = user_data.user_data.all().order_by('-id')
    print(chat_data)
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        response = get_response(prompt)
        ChatData.objects.create(user_chat=user_data, prompt=prompt, response=response)
    return render(request, 'chat.html', {'chat_data': chat_data})






