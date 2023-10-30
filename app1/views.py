from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *
# Create your views here.


def student(request):
    s = Student.objects.all()
    soz = request.GET.get("qidiruv_sozi")
    if soz is not None:
         s = Student.objects.filter(ism__contains=soz)
    data = {
        "student": s
    }
    return render(request, 'studentlar.html', data)

def reja(request):
    r = Reja.objects.all()
    soz = request.GET.get("qidiruv_sozi")
    if soz is not None:
        r = Reja.objects.filter(sarlavhasi__contains=soz)
    forma = RejaForm(request.POST)
    if request.method == 'POST':
        if forma.is_valid():
            forma.save()
            return redirect('/rejalar/')
    data = {
        "reja": r,
        'form': RejaForm
    }
    return render(request, 'rejalar.html', data)

def bajarilmagan(request):
    data = {
        "reja": Reja.objects.filter(bajarilgan=True)
    }
    return render(request, 'bajarilmagan.html', data)


def kamida(request):
    data = {
        'student': Student.objects.filter(kurs__gte=3)
    }
    return render(request, 'kurs.html', data)

def reja_ochir(request, son):
    Reja.objects.filter(id=son).delete()
    return redirect("/rejalar")

def yosh(request):
    data = {
        'student': Student.objects.filter(yosh__gt=20)
    }
    return render(request, 'yoshi_katta.html', data)

def bitiruvchilar_rejalari(request):
    x = Student.objects.filter(kurs__gte=4)
    data = {
        'student': Reja.objects.filter(student__in=x)
    }
    return render(request, 'bitiruvchilar_rejalari.html', data)

def tanlangan_student(request, son):
    x = Student.objects.get(id=son)
    data = {
        "reja": Reja.objects.filter(student=x)
    }
    return render(request, 'tanlangan_rejalar.html', data)

