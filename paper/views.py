from django.shortcuts import render, get_object_or_404
from .models import Paper, Method


def paper_view(request, paper_id):
    paper = get_object_or_404(Paper, pk=paper_id)
    context = {'paper': paper}
    return render(request, "paper/paper.html", context)


def method_view(request, method_id):
    method = get_object_or_404(Method, pk=method_id)
    context = {'method': method}
    return render(request, "paper/method.html", context)
