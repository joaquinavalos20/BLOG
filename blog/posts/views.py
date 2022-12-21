from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm

def index(request):
    post = Post.objects.all()

    return render(request, "index.html",{"post":post})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)

    comments = post.comments.filter(active=True)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = post
            new_form.save()
            return HttpResponseRedirect("#")
    else:
        form = CommentForm

    return render(request, "post_detail.html",{"post":post, "comments":comments, "form":form})