from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag
from django.db.models import F
from .forms import PostsForm

class Home(ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
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


class PostsByCategory(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context
    

class GetPost(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context
    

class PostsByTag(ListView):
    pass

def add_news(request):
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = PostsForm()
    return render(request, 'blog/add_news.html', {'form': form})