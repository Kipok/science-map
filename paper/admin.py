from django.contrib import admin
from .models import Paper, Method


class PaperAdmin(admin.ModelAdmin):
    pass

# TODO: make problem field shorter

class MethodAdmin(admin.ModelAdmin):
    pass


admin.site.register(Paper, PaperAdmin)
admin.site.register(Method, MethodAdmin)
