from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentlar/', student),
    path('rejalar/', reja),
    path('bacharilmagan/', reja),
    path('uch/', kamida),
    path('uch/', kamida),
    path('reja_ochir/<int:son>/', reja_ochir),
    path('yoshi_kattalar/', yosh),
    path('bitiruvchilar_rejalari/', bitiruvchilar_rejalari),
    path('tanlangan_student/<int:son>/', tanlangan_student),
    path('', asosiy),
]
