from django.shortcuts import render

# Create your views here.
def show_hobby(request):
    return render(request, 'Hobby/hobby.html')