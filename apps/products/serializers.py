from rest_framework import serializers
from .models import Product, ProductViews

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id", 
            "user", 
            "title", 
            "slug",
            "ref_code",
            "product_type",
            "description",
            "price",
            "tax",
            "final_product_price",
            "cover_photo",
            "photo1",
            "photo2",
            "photo3",
            "photo4",
            "published_status",
            "views",
            ]
        def get_user(self,obj):
            return obj.user.username
class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ["updated_at", "pkid"]
class ProductViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductViews
        exclude = ["updated_at", "pkid"]