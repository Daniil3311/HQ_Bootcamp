from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User


CHOICES_ACCESS = [
    ('N', 'no'),
    ('Y', 'yes'),
]


class Product(models.Model):
    author = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    time_start = models.DateTimeField(default=0)
    max_quantity_students = models.IntegerField()
    min_quantity_students = models.IntegerField(default=5)
    quantity_students = models.IntegerField(blank=True, null=True)
    lesson = models.ManyToManyField('Lesson', related_name='lesson', blank=True, null=True)


class Human(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Student(models.Model):
    name = models.CharField(max_length=50)


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(blank=True)
    product = models.ManyToManyField(Product, related_name='product', blank=True, null=True)


class Groups(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name_group = models.CharField(max_length=50)
    students = models.ManyToManyField(Student,  blank=True, null=True)


class AccessProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    access = models.CharField(max_length=1, choices=CHOICES_ACCESS)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True)
