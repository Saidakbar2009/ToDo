from django.contrib import admin
from .models import *
from django.contrib.auth.models import *
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['ism', 'kurs', 'yosh', 'student_raqam']
    search_fields = ['ism']
    search_help_text = "ism bo'yicha qidiring"
    list_filter = ['kurs']
    list_display_links = ['ism']

@admin.register(Reja)
class RejaAdmin(admin.ModelAdmin):
    list_display = ['sarlavhasi', 'sana', 'batafsil', 'bajarilgan', 'student']
    list_filter = ['bajarilgan']
    search_fields = ['sarlavhasi']
    search_help_text = 'sarlavhasi boyicha qidiring'
    list_display_links = ['sarlavhasi']
    autocomplete_fields = ['student']

# admin.site.register(Student)
# admin.site.register(Reja)
