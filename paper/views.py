from django.shortcuts import render


def paper_page(request):
    return render(request, "paper/paper.html", {})
