from rest_framework import serializers
from app.models import Product, Student, Groups, Lesson, AccessProduct
from rest_framework.exceptions import ValidationError


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        lessons = validated_data['lesson']
        # lesson.product.set(products)
        print(lessons)
        p = Product.objects.create(name=validated_data['name'], quantity_students=Student.objects.count(), max_quantity_students=3)
        p.lesson.set(lessons)
        p.save()
        return p


class StudentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class LessonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'

    def create(self, validated_data):
        products = validated_data.pop('product')
        lesson = Lesson.objects.create(**validated_data)
        lesson.product.set(products)
        p=Product.objects.filter(pk=products[0].id)
        p[0].lesson.add(lesson)
        # print(p)
        return lesson


class AccessProductSerializers(serializers.ModelSerializer):
    lessons = LessonSerializers(many=True, read_only=True)

    class Meta:
        model = AccessProduct
        fields = '__all__'

    # def create(self, validated_data):
    #     profile_data = validated_data.pop('lessons')
    #     access = AccessProduct.objects.create(**validated_data)
    #     Lesson.objects.create(**profile_data)
    #     return access

class GroupSerializers(serializers.ModelSerializer):
    # product = ProductSerializers(many=True)

    class Meta:
        model = Groups
        fields = ['id', 'product', 'name_group', 'students']

    # def create(self, validated_data):
    #     # print(validated_data['students'][0].access)
    #     if validated_data['students'][0].access == 'N' or "0":
    #         raise serializers.ValidationError('Нет доступа')
    #     else:
    #         return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     # достаем связанные данные для других таблиц
    #     positions = validated_data.pop('positions')
    #     # обновляем склад по его параметрам
    #     stock = super().update(instance, validated_data)
    #     # здесь вам надо обновить связанные таблицы
    #     # в нашем случае: таблицу StockProduct
    #     # с помощью списка positions
    #     for element in positions:
    #         obj, created = StockProduct.objects.update_or_create(
    #             stock=stock,
    #             product=element['product'],
    #             defaults={'stock': stock, 'product': element['product'], 'quantity': element['quantity'],
    #                       'price': element['price']}
    #         )
    #     return stock




