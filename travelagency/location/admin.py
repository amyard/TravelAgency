from django.contrib import admin
from .models import Country

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['title', 'title_en', 'title_de']
    search_fields = ['title', 'title_en', 'title_de']
    prepopilated_fields = {'slug':('title'),}

    fieldsets = (
        ('Title', {'fields':('title', 'title_en', 'title_de',)}),
    )