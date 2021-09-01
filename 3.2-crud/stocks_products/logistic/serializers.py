from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def validate_positions(self, value):
        if not value:
            raise ValidationError('пустой список продуктов')
        return value

    def create(self, validated_data):
        positions = validated_data.pop('positions')

        stock = super().create(validated_data)

        for item in positions:
            StockProduct.objects.create(stock=stock, **item)

        return stock

    def update(self, instance, validated_data):
        # старые данные
        product_items_dict = dict((i.id, i) for i in instance.products.all())

        # новые данные
        positions_new = validated_data.pop('positions')

        stock = super().update(instance, validated_data)

        for item in positions_new:
            StockProduct.objects.update_or_create(stock=instance, product=item["product"], defaults={**item})

            # if item["product"].id in product_items_dict.keys():
            #     # если продукт есть на складе, то обновляем данные по нему
            #     product_items_dict.pop(item["product"].id)
            #     StockProduct.objects.filter(stock=instance.id, product=item["product"].id).update(**item)
            # else:
            #     # если продукта нет, то добавляем его на склад
            #     StockProduct.objects.create(stock=instance, **item)

        return stock
