from django import forms
from elements.models import Paper


class PaperSearchForm(forms.Form):
  paper = forms.ModelChoiceField(Paper.objects.all())
