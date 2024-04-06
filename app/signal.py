from django.core.signals import request_finished
from django.dispatch import receiver
import django.dispatch
from app.models import AccessProduct, Groups


new_signal = django.dispatch.Signal('access_product')


# @receiver(new_signal)
def my_callback(sender, access_product, **kwargs):

    # здесь находим в группе продукт где был изменен статус у студента access
    g=Groups.objects.filter(product=access_product.product)
    for g1 in g:
        if g1.product.min_quantity_students > g1.students.count():
            g1.students.add(access_product.student)
            print(g1.students.count())
            break
        else:
            continue

    print("Request finished!")
    # print(g.students.add(access_product.student))
    print(access_product)


new_signal.connect(my_callback, dispatch_uid="my_unique_identifier")