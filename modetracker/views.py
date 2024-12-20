from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import DailyFeeling
from django.contrib.auth.decorators import login_required
from datetime import date
from django.http import JsonResponse

@login_required
def mode_tracker(request):
    today = date.today()
    message = ''
    if request.method == 'POST':
        usermode = request.POST.get('usermode')
        daily_feeling, created = DailyFeeling.objects.get_or_create(user=request.user, date=today)
        daily_feeling.feeling = usermode
        daily_feeling.save()
        message = 'Your feeling has been recorded.' if created else 'Your feeling has been updated.'
        
        # return render(request, 'mode_tracker.html', {'message': message, 'usermode': usermode})
    
    daily_feeling = DailyFeeling.objects.filter(user=request.user).latest('date')
    if str(daily_feeling.date) == str(today):
        print('done')
        usermode = daily_feeling.feeling
    else:
        print('ndone')
        usermode = ''
    return render(request, 'mode_tracker.html', {'today': today, 'usermode':usermode, 'message': message,})

def get_mode(request):
    today = date.today()
    daily_feeling = DailyFeeling.objects.filter(user=request.user).latest('date')
    if str(daily_feeling.date) == str(today):
        usermode = daily_feeling.feeling
    else:
        usermode = ''
    return JsonResponse({'usermode': usermode})