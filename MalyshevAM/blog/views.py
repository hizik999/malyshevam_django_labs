from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class Home(ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница/Classic Blog Design'
        return context

# Create your views here.
def index(request):
    return render(request, 'praktikums/index.html')

def praktikum2(request):
    return render(request, 'praktikums/praktikum2.html')

def praktikum3_1(request):
    return render(request, 'praktikums/praktikum3_1.html')

def praktikum3_2(request):
    return render(request, 'praktikums/praktikum3_2.html')

def praktikum3_3(request):
    return render(request, 'praktikums/praktikum3_3.html')

def praktikum4_1(request):
    return render(request, 'praktikums/praktikum4_1.html')

def praktikum4_2(request):
    return render(request, 'praktikums/praktikum4_2.html')

def praktikum4_3(request):
    return render(request, 'praktikums/praktikum4_3.html')

def praktikum4_4(request):
    return render(request, 'praktikums/praktikum4_4.html')

def praktikum5(request):
    return render(request, 'praktikums/praktikum5.html')

def blog_index(request):
    return render(request, 'blog/index.html')

def praktikum7(request):
    return render(request, 'praktikums/praktikum7.html')

def praktikum8(request):
    return render(request, 'praktikums/praktikum8.html')

def praktikum9_1(request):
    return render(request, 'praktikums/praktikum9_1.html')

def praktikum9_2(request):
    return render(request, 'praktikums/praktikum9_2.html')

def praktikum9_3(request):
    return render(request, 'praktikums/praktikum9_3.html')

def praktikum9_4(request):
    return render(request, 'praktikums/praktikum9_4.html')

def blog_category(request, slug):
    return render(request, 'blog/category.html')

def blog_post(request, slug):
    return render(request, 'blog/post.html')