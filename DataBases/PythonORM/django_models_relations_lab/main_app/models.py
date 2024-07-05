from datetime import date

from django.db import models
from django.db.models import SET_NULL, CASCADE


# Create your models here.

class Lecturer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    lecturer = models.ForeignKey(to='Lecturer', on_delete=SET_NULL, null=True,blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    student_id = models.CharField(max_length=10,primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    subjects = models.ManyToManyField(to='Subject', through='StudentEnrollment')

class StudentEnrollment(models.Model):

    class GradeChoices(models.TextChoices):
        A = "A", "A"
        B = "B", "B"
        C = "C", "C"
        D = "D", "D"
        F = "F", "F"

    student = models.ForeignKey(to='Student',on_delete=CASCADE)
    subject = models.ForeignKey(to='Subject',on_delete=CASCADE)
    enrollment_date = models.DateField(default=date.today())
    grade = models.CharField(max_length=1, choices=GradeChoices.choices)


class LecturerProfile(models.Model):
    lecturer = models.OneToOneField(to='Lecturer', on_delete=CASCADE)
    email = models.EmailField(unique=True)
    bio=models.TextField(null=True, blank=True)
    office_location = models.CharField(max_length=100, blank=True, null=True)



