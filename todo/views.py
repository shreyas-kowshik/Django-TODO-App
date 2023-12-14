from django.shortcuts import render
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def welcome(request):
    return render(request, 'todo/welcome.html', {})

def todo_list(request):
    # Populate all posts of current user
    # posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    posts = Post.objects.all()
    return render(request, 'todo/todo_view.html', {'posts':posts})

def todo_create(request):
    # Open a form for user to type in and allow saving
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.last_modified_date = timezone.now()
            post.save()
            return redirect('todolist')
    else:
        form = PostForm()
    return render(request, 'todo/todo_create.html', {'form': form})