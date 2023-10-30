from django.db import models

# Create your models here.
class Student(models.Model):
    ism = models.CharField(max_length=30)
    kurs = models.PositiveSmallIntegerField()
    yosh = models.PositiveSmallIntegerField()
    student_raqam = models.PositiveSmallIntegerField(unique=True)
    def __str__(self):
        return self.ism

class Reja(models.Model):
    sarlavhasi = models.CharField(max_length=100)
    sana = models.DateField()
    batafsil = models.CharField(max_length=500, blank=True, null=True)
    bajarilgan = models.BooleanField(default=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.sarlavhasi
