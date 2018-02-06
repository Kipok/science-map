from django.shortcuts import render, get_object_or_404
from .models import Paper


def paper_view(request, paper_id):
    paper = get_object_or_404(Paper, pk=paper_id)
    context = {'paper': paper}
    return render(request, "paper/paper.html", context)
