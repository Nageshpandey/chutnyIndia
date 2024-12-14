from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.core.validators import MinValueValidator


# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.city
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.city)
        super().save(*args, **kwargs)

class OnLocation(models.Model):
    onlocation = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    number = models.CharField(max_length=50, null=True, blank=True)
    event_location = models.CharField(max_length=50, null=True, blank=True)
    attandence = models.IntegerField(null=True, blank=True)
    date = models.DateField(default=timezone.now)
    message = models.TextField(null=True, blank=True)
    contact_number = models.CharField(max_length=15, default='')
    email_address = models.EmailField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.onlocation

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.onlocation)
        super().save(*args, **kwargs)

    def get_slider_images(self):
        return OnLocationImage.objects.filter(onlocation=self)


class Category(models.Model):
    location =models.ForeignKey(Location, on_delete=models.CASCADE)
    page_content = models.TextField(null=True, blank=True)
    menu_name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.menu_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.menu_name)
        super().save(*args, **kwargs)

class Image(models.Model):
    location =models.ForeignKey(Location, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

class OnLocationImage(models.Model):
    onlocation =models.ForeignKey(OnLocation, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    onlocation = models.ForeignKey(OnLocation, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"Image {self.id} for {self.onlocation}"

class Menu(models.Model):
    sub_menu = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="sub_menu")
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    menu_details = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)
    menu_position = models.IntegerField(default=0, validators=[MinValueValidator(-999)])  # Allow negative values

    class Meta:
        ordering = ['menu_position']  # Order by menu_position by default

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @classmethod
    def get_ordered_menus(cls):
        return cls.objects.all()  # This will return menus ordered by menu_position due to the Meta class


class Address(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="address")
    email = models.EmailField( max_length=254, null=True, blank=True)
    full_add = models.TextField( null=True, blank=True)
    mobile_number = models.CharField( max_length=50, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    def __str__(self):
        return self.email
    

class ContactUs(models.Model):
    name = models.CharField( max_length=50)
    number = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    event_location = models.CharField( max_length=50, null=True, blank=True)
    attandence = models.IntegerField( null=True, blank=True)
    date = models.DateField( auto_now=False, auto_now_add=False)
    message = models.TextField(  null=True, blank=True)


    def __str__(self):
        return self.name
    
class Event(models.Model):
    onlocation = models.ForeignKey(OnLocation, on_delete=models.CASCADE, related_name='events')
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.event_name
    