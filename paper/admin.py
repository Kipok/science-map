from django.contrib import admin
from .models import Paper, Method, Author


class AuthorAdmin(admin.ModelAdmin):
    pass


class MethodInline(admin.TabularInline):
    model = Method
    extra = 1


class PaperAdmin(admin.ModelAdmin):
    inlines = [MethodInline]


# TODO: make problem field shorter


admin.site.register(Paper, PaperAdmin)
admin.site.register(Author, AuthorAdmin)
