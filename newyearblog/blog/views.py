from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {
        'posts': posts,
        'title': 'Главная страница',
    })


def about(request):
    return render(request, 'blog/about-us.html')

def create(request):
    error = ''
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = "Форма заполнена неверно"
    form = PostForm(request.POST or None)
    context = {
        "form": form,
        "error": error
    }
    return render(request, 'blog/create.html', context)