from rest_framework.permissions import BasePermission
from app.models import AccessProduct, Lesson


class IsAccess(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            ap = AccessProduct.objects.filter(access='Y', student=1)
            # l = Lesson.objects.filter(product=ap.id)

            for a in ap:
                # print(a.product)
                lesson = Lesson.objects.filter(product=a.product)
                # print(obj.product.all())

                return lesson




