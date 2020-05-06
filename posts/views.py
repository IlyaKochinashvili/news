from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post
from django.shortcuts import render, redirect


def index(request):
    posts = Post.objects.filter(approved=True)
    context = {'posts': posts}
    return render(request, 'index.html', context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_created = form.save()
            post_created.author = request.user
            if request.user.groups.filter(name__in=('admins', 'redactors')).exists():
                post_created.approved = True
                post_created.moderated = True
            post_created.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})


@login_required
def create_comment(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_created = form.save()
            comment_created.author = request.user
            comment_created.post_id = post_id
            comment_created.save()
            return redirect('index')
    else:
        form = CommentForm()
    return render(request, 'comment.html', {'form': form})
