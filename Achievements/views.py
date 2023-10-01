from django.shortcuts import render

# Create your views here.
def show_achievements(request):
    return render(request, 'Achievements/achievements.html')