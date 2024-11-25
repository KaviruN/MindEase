from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import DailyFeeling

# Create your views here.

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import DailyFeeling

# Create your views here.

from django.contrib.auth.decorators import login_required
from .models import DailyFeeling

# Create your views here.

@login_required
def mode_tracker(request):
    if request.method == 'POST':
        usermode = request.POST.get('usermode')
        daily_feeling, created = DailyFeeling.objects.get_or_create(user=request.user)
        daily_feeling.feeling = usermode
        daily_feeling.save()
        message = 'Your feeling has been recorded.' if created else 'Your feeling has been updated.'
        
        return render(request, 'mode_tracker.html', {'message': message, 'usermode': usermode})
    
    daily_feeling = DailyFeeling.objects.filter(user=request.user).first()
    usermode = daily_feeling.feeling if daily_feeling else None
    return render(request, 'mode_tracker.html', {'usermode': usermode})