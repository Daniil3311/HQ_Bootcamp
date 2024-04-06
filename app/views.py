from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app.models import Product, Student, Groups, Lesson, AccessProduct
from app.serializers import ProductSerializers, StudentSerializers, GroupSerializers, LessonSerializers, AccessProductSerializers
from app.permission import IsAccess
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from app.filter import LessonFilter
from django_filters.rest_framework import DjangoFilterBackend
from app.signal import new_signal


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    # quantity_student = Student.objects.count()

    def get_queryset(self):
        ap = Product.objects.all()
        # for a in ap:
        #     # print(a.product.id)
        #     # print(lesson[0])
        #     lesson = Lesson.objects.filter(product=a.product)
        #     print(lesson)
        return ap


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class GroupsViewSet(ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupSerializers


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    # permission_classes = [IsAdmin]
    filterset_class = LessonFilter
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        ap = AccessProduct.objects.filter(access='Y')
        for a in ap:
            lesson = Lesson.objects.filter(product=a.product)
            # print(lesson)
            # ace = AccessProduct.objects.filter(student=2).update(access='N')
            # print(ace)

            return lesson


class AccessProductViewSet(ModelViewSet):
    queryset = AccessProduct.objects.all()
    serializer_class = AccessProductSerializers
    # permission_classes = [IsAccessReadOnly]











