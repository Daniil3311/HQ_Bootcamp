from django.contrib import admin
from app.models import Product, Student, Groups, Lesson, AccessProduct
from app.signal import new_signal


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    pass


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


@admin.register(AccessProduct)
class AccessProductAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.access == 'Y':
            print(obj.student)
            new_signal.send(sender=self.__class__, access_product=obj)
