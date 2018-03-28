from django.shortcuts import render, get_object_or_404
from .models import Paper, Method


def paper_view(request, paper_id):
    paper = get_object_or_404(Paper, pk=paper_id)
    context = {
        'paper': paper,
        'methods': Method.objects.filter(orig_paper_id=paper_id),
    }
    return render(request, "elements/paper.html", context)


def method_view(request, method_id):
    method = get_object_or_404(Method, pk=method_id)
    context = {'method': method}
    return render(request, "elements/method.html", context)
