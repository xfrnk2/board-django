from django.shortcuts import render
def screen(request):
    return render(request, 'main_screen/root.html')