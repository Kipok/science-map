from django.contrib import admin
from .models import Paper, Method, Author, Conference, \
                    ValueResult, TextResult, Dataset, Metric,\
                    Link, LinkType, PaperType, Authorship


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  pass


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
  pass


@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
  pass


class MethodInline(admin.TabularInline):
  model = Method
  extra = 1


class ValueResultInline(admin.TabularInline):
  model = ValueResult
  extra = 1


class TextResultInline(admin.TabularInline):
  model = TextResult
  extra = 1


class LinkInline(admin.TabularInline):
  model = Link
  extra = 1
  fk_name = 'src_paper'


class AuthorshipInline(admin.TabularInline):
  model = Authorship
  extra = 1


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
  # TODO: make problem field shorter
  inlines = [AuthorshipInline, MethodInline, ValueResultInline, 
             TextResultInline, LinkInline]


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
  pass


@admin.register(LinkType)
class LinkTypeAdmin(admin.ModelAdmin):
  pass


@admin.register(PaperType)
class PaperTypeAdmin(admin.ModelAdmin):
  pass
