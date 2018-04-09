from django.shortcuts import render, redirect, reverse
from .forms import PaperSearchForm
from elements.models import Paper


def home_page(request):
  if request.method == 'POST':
    form = PaperSearchForm(request.POST)
    if form.is_valid():
      paper_id = form.cleaned_data['paper'].id
      return redirect(reverse('elements:paper', kwargs={'paper_id': paper_id}))
  else:
    form = PaperSearchForm()
  all_papers = Paper.objects.all()
  return render(request, "home/home.html", {'form': form,
                                            'all_papers': all_papers})
