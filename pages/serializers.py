from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField() 
    class Meta:
        model = Category
        fields = ["id", 'menu_name', "slug", "image"]

    def get_image_url(self, obj):
        print(self.context,";llllllllllll")
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):  # Assuming you have an Image model
    image_url = serializers.SerializerMethodField()  # Full URL for the image

    class Meta:
        model = Image  # Your Image model
        fields = ['id', 'image_url']  # Include other fields as needed

    def get_image_url(self, obj):
        request = self.context.get('request')
        if request and obj.image:  # Ensure image field exists
            return request.build_absolute_uri(obj.image.url)
        return None

class LocationSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    slider_images = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = '__all__'

    def get_categories(self, obj):
        if obj:
            cat = Category.objects.filter(location=obj)
            serlizer = CategorySerializer(cat, many=True, context=self.context)
            return serlizer.data
        else:
            return []

    def get_address(self, obj):
        if obj:
            address = Address.objects.filter(location=obj).last()
            serlizer = AddressSerializer(address)
            return serlizer.data
        else:
            return {}

    def get_slider_images(self, obj):
        if obj:
            img = Image.objects.filter(location=obj)
            serlizer = ImageSerializer(img, many=True, context=self.context)
            return serlizer.data
        else:
            return []



class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class CategoryRetriveSerializer(serializers.ModelSerializer):
    menu_list = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = "__all__"
        
    def get_menu_list(self, obj):
        if obj:
            menu = Menu.objects.filter(sub_menu=obj)
            return  MenuSerializer(menu, many=True).data
        return []


