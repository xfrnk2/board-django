from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.
from django.shortcuts import render
def userinfo(request):
    return render(request, 'users/userinfo.html')

def mypage(request):
    current_user = request.user
    if current_user.is_authenticated:
        return render(request, 'users/mypage.html', {'q': current_user.id})
    else:
        return render(request, 'users/mypage.html', {'q': '없지룽'})