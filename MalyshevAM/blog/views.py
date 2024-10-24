from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def praktikum2(request):
    return render(request, 'blog/praktikum2.html')

def praktikum3_1(request):
    return render(request, 'blog/praktikum3_1.html')

def praktikum3_2(request):
    return render(request, 'blog/praktikum3_2.html')

def praktikum3_3(request):
    return render(request, 'blog/praktikum3_3.html')