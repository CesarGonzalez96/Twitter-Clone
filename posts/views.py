from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from cloudinary.forms import cl_init_js_callbacks


def index(request):
    # if method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
    # Form is valid
        if form.is_valid():
            # yes save
            form.save()
        # redirect home
            return HttpResponseRedirect('/')
        # no show error
        else:
            return HttpResponseRedirect(form.errors.as_json())
    # Get posts, limit 20
    posts = Post.objects.all()[:20]

    # show
    return render(request, 'posts.html',
                  {'posts': posts})


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


def like(request, post_id):
    post = Post.objects.get(id=post_id)
    post.likes = post.likes + 1
    post.save()
    return HttpResponseRedirect('/')


def dislike(request, post_id):
    post = Post.objects.get(id=post_id)
    post.likes = post.likes - 1
    post.save()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    if request.method == "GET":
        posts = Post.objects.get(id=post_id)
        posts.delete()
        return render(request, "edit.html", {"posts": posts})
    if request.method == "POST":
        editposts = Post.objects.get(id=post_id)
        form = PostForm(request.POST, request.FILES, instance=editposts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("not valid")
