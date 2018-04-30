from django.contrib import admin
from .models import Paper, Method, Author, Conference, \
                    Result, Dataset, Metric, Link, LinkType, PaperType


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


class ResultInline(admin.TabularInline):
  model = Result
  extra = 1


class LinkInline(admin.TabularInline):
  model = Link
  extra = 1
  fk_name = 'src_paper'


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
  # TODO: make problem field shorter
  inlines = [MethodInline, ResultInline, LinkInline]


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
  pass


@admin.register(LinkType)
class LinkTypeAdmin(admin.ModelAdmin):
  pass


@admin.register(PaperType)
class PaperTypeAdmin(admin.ModelAdmin):
  pass
