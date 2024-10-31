from django.db import models

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

class Menu(models.Model):
    sub_menu = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="sub_menu")
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    menu_details = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.menu_name)
        super().save(*args, **kwargs)


class Address(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="address")
    email = models.EmailField( max_length=254, null=True, blank=True)
    full_add = models.TextField( null=True, blank=True)
    mobile_number = models.CharField( max_length=50, null=True, blank=True)

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
    