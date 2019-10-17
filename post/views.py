from django.shortcuts import render, HttpResponse, get_object_or_404,HttpResponseRedirect,redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

def postIndex(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})


def postDetail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }
    return render(request, 'post/detail.html', context)


def postCreate(request):
    # if request.method == "POST":
    #   form = PostForm(request.POST)
    #   if form.is_valid():
    #       form.save()

    # else:
    #   form = PostForm()

    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save()
        messages.success(request, 'Post is created successfully!')
        return HttpResponseRedirect(post.getAbsoluteURL())

    context = {
        'form': form,
    }

    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # Post.objects.create(title = title, content = content)

    return render(request, 'post/form.html', context)


def postUpdate(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Post is updated successfully!', extra_tags='message-success')
        return HttpResponseRedirect(post.getAbsoluteURL())

    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)

def postDelete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post:index')
