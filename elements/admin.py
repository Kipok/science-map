from django.contrib import admin
from .models import Paper, Method, Author, Conference, Result


class AuthorAdmin(admin.ModelAdmin):
  pass


class MethodInline(admin.TabularInline):
  model = Method
  extra = 1


class ResultInline(admin.TabularInline):
  model = Result
  extra = 1


class PaperAdmin(admin.ModelAdmin):
  inlines = [MethodInline, ResultInline]


class ConferenceAdmin(admin.ModelAdmin):
  pass


# TODO: make problem field shorter


admin.site.register(Paper, PaperAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Conference, ConferenceAdmin)
