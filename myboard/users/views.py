from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def userinfo(request):
    return render(request, 'users/userinfo.html')