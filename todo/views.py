from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Blog
from .forms import BlogForm


def create_view(request):

    context = {}

    form = BlogForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("list-view")

    context["form"] = form
    context["title"] = "Create View"
    return render(request, "todo/create_view.html", context)


def list_view(request):

    context = {}

    context["blogs"] = Blog.objects.all()
    context["title"] = "List View"
    return render(request, "todo/list_view.html", context)


def detail_view(request, id):

    context = {}

    context["data"] = Blog.objects.get(id=id)
    context["title"] = "Detail View"
    return render(request, "todo/detail_view.html", context)


def update_view(request, id):

    context = {}

    obj = get_object_or_404(Blog, id=id)

    form = BlogForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("list-view")

    context["form"] = form
    context["title"] = "Update View"
    return render(request, "todo/update_view.html", context)


def delete_view(request, id):

    context = {}

    obj = get_object_or_404(Blog, id=id)

    obj.delete()

    return redirect("list-view")
