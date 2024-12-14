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

class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(source='image')  # Assuming 'image' is the field name in your Image model

    class Meta:
        model = Image
        fields = ['id', 'image_url']  # Include the id and image_url

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

    def update(self, instance, validated_data):
        # Update the instance with the new data
        instance.menu_position = validated_data.get('menu_position', instance.menu_position)
        instance.save()

        # Update other menus' positions if needed (e.g., shifting positions)
        Menu.objects.filter(menu_position=instance.menu_position).exclude(id=instance.id).update(menu_position=instance.menu_position + 1)

        return instance


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

class OnLocationImageSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(source='image')  # Assuming 'image' is the field name
    onlocation = serializers.PrimaryKeyRelatedField(queryset=OnLocation.objects.all(), default=1)  # Use PrimaryKeyRelatedField

    class Meta:
        model = OnLocationImage
        fields = ['id', 'image_url', 'onlocation']  # Include the id, image_url, and onlocation

class OnLocationSerializer(serializers.ModelSerializer):
    slider_images = OnLocationImageSerializer(many=True, read_only=True, source='onlocationimage_set')

    class Meta:
        model = OnLocation
        fields = '__all__'


