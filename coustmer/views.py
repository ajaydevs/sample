from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'coustmer/home.html')

def profile(request):
    return render(request, 'coustmer/profile.html')