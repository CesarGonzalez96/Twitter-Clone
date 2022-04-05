from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm


def index(request):

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():

            form.save()

            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect(form.errors.as_json())

    posts = Post.objects.all().order_by('-created_at')[:20]
    return render(request, 'posts.html',
                  {'posts': posts})
