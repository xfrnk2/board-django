from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def main(request):
    current_user = request.user
    q = '로그인'
    if current_user.is_authenticated:
        q = '로그아웃'
    return render(request, 'main.html', {'login_status': q})
