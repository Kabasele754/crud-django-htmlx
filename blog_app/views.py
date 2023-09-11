import json

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from .models import Blog
from .forms import BlogForm


def index(request):
    return render(request, 'pages/index.html')


def blog_list(request):
    return render(request, 'pages/blog_list.html', {
        'blogs': Blog.objects.all(),
    })


def add_movie(request):
    if request.method == "POST":
        form = BlogForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']

            blogpost = form.save(commit=False)
            blogpost.title = title
            blogpost.description = description
            blogpost.image = image
            blogpost.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "blogListChanged": None,
                        "showMessage": f"{blogpost.title} added."
                    })
                })
    else:
        form = BlogForm()
    return render(request, 'pages/blog_form.html', {
        'form': form,
    })


def edit_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(data=request.POST, files=request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "blogListChanged": None,
                        "showMessage": f"{blog.title} updated."
                    })
                }
            )
    else:
        form = BlogForm(instance=blog)
    return render(request, 'pages/blog_form.html', {
        'form': form,
        'blog': blog,
    })


@require_POST
def remove_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "blogListChanged": None,
                "showMessage": f"{blog.title} deleted."
            })
        })
