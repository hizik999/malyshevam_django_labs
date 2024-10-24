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

def praktikum4_1(request):
    return render(request, 'blog/praktikum4_1.html')

def praktikum4_2(request):
    return render(request, 'blog/praktikum4_2.html')

def praktikum4_3(request):
    return render(request, 'blog/praktikum4_3.html')

def praktikum4_4(request):
    return render(request, 'blog/praktikum4_4.html')

