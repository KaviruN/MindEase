from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import DailyFeeling
from datetime import date
from django.http import JsonResponse,HttpResponse


def mode_tracker(request):
    if not request.user.is_authenticated:
        return redirect('user_auth:sign_in')
    today = date.today()
    return render(request, 'mode_tracker.html', {'today': today})

def get_mode(request):
    if request.user.is_authenticated:
        today = date.today()
        daily_feeling = DailyFeeling.objects.filter(user=request.user).latest('date')
        if str(daily_feeling.date) == str(today):
            usermode = daily_feeling.feeling
        else:
            usermode = ''
        return JsonResponse({'usermode': usermode})
    
def save_mode(request):
    today = date.today()
    message = ''
    if request.method == 'POST':
        usermode = request.POST.get('usermode')
        daily_feeling, created = DailyFeeling.objects.get_or_create(user=request.user, date=today)
        daily_feeling.feeling = usermode
        daily_feeling.save()
        return ('Your feeling has been recorded.' if created else 'Your feeling has been updated.')