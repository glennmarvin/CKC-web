from django.db import models
from django.contrib.auth.models import User
# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete, pre_save
from django.dispatch.dispatcher import receiver


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)
    catid = models.CharField(max_length=100, help_text="The following categories are available: 'bicycle' for bicycle products, 'cutlery' for cutlery, 'toys' for toys, 'cups' for coffee cups and 'packaging' for packaging. Want another category added? Contact Glenn.")

    class Meta: 
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category

class Product(models.Model):
    name = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='products/', max_length=255)
    image2 = models.ImageField(upload_to='products/', max_length=255)
    image3 = models.ImageField(upload_to='products/', max_length=255)
    description = models.TextField(help_text="Does accept raw HTML text.")
    subtitle = models.CharField(max_length=300, blank=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    class Meta: 
        verbose_name = "Product"
        verbose_name_plural = "Products"
    def __str__(self):
        return self.name

class Services(models.Model):
    headline = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='services/', max_length=255)
    text = models.TextField(blank=True)
    class Meta: 
        verbose_name = "Service"
        verbose_name_plural = "Services"
    def __str__(self):
        return self.headline


class Billboard(models.Model):
    headline = models.CharField(max_length=30, blank=True)
    subtitle = models.CharField(max_length=50, blank=True)
    typewriter = models.BooleanField(default=True, help_text="To turn on / off typewriter effect on the billboard. Only works for the first billboard element (not for the other slides).")
    image = models.ImageField(upload_to='billboard/', max_length=255)
    textcolor = models.CharField(max_length=7, blank=True, help_text="Sets the text color on the billboard. Please provide the hex code: e.g. #000000. Is black by default.")
    class Meta: 
        verbose_name = "Billboard"
        verbose_name_plural = "Billboard"

class AboutUs(models.Model):
    maintext = models.TextField()

    class Meta: 
        verbose_name = "About us"
        verbose_name_plural = "About us"
    

##### To delete images after deleting / updating them. They take up too much space.
## Products
@receiver(pre_delete, sender=Product)
def product_delete(sender, instance, **kwargs):
    try:
        # is the object in the database yet?
        Product.objects.get(id=instance.id)
        # Pass false so FileField doesn't save the model.
        instance.image1.delete(False)
        instance.image2.delete(False)
        instance.image3.delete(False)
    except Product.DoesNotExist:
        # object is not in db, nothing to worry about
        return

## Services
@receiver(pre_delete, sender=Services)
def services_delete(sender, instance, **kwargs):
    try:
        # is the object in the database yet?
        Services.objects.get(id=instance.id)
        # Pass false so FileField doesn't save the model.
        instance.image.delete(False)
    except Services.DoesNotExist:
        # object is not in db, nothing to worry about
        return

## Billboard
@receiver(pre_delete, sender=Billboard)
def billboard_delete(sender, instance, **kwargs):
    try:
        # is the object in the database yet?
        Billboard.objects.get(id=instance.id)
        # Pass false so FileField doesn't save the model.
        instance.image.delete(False)
    except Billboard.DoesNotExist:
        # object is not in db, nothing to worry about
        return

##### Want to do the same on update, don't want to keep old images.
## Products
@receiver(pre_save, sender=Product)
def product_update(sender, instance, **kwargs):
    try:
        # is the object in the database yet?
        obj = Product.objects.get(id=instance.id)
    except Product.DoesNotExist:
        # object is not in db, nothing to worry about
        return
    
    if obj.image1 and instance.image1 and obj.image1 != instance.image1:
        # Pass false so FileField doesn't save the model.
        obj.image1.delete()

    if obj.image2 and instance.image2 and obj.image2 != instance.image2:
        # Pass false so FileField doesn't save the model.
        obj.image2.delete()


    if obj.image3 and instance.image3 and obj.image3 != instance.image3:
        # Pass false so FileField doesn't save the model.
        obj.image3.delete()

## Services
@receiver(pre_save, sender=Services)
def services_update(sender, instance, **kwargs):
    try:
        # is the object in the database yet?
        obj = Services.objects.get(id=instance.id)
    except Services.DoesNotExist:
        # object is not in db, nothing to worry about
        return
    
    if obj.image and instance.image and obj.image != instance.image:
        # Pass false so FileField doesn't save the model.
        obj.image.delete()


## Billboard
@receiver(pre_save, sender=Billboard)
def billboard_update(sender, instance, **kwargs):
    try:
        # is the object in the database yet?
        obj = Billboard.objects.get(id=instance.id)
    except Billboard.DoesNotExist:
        # object is not in db, nothing to worry about
        return
    
    if obj.image and instance.image and obj.image != instance.image:
        # Pass false so FileField doesn't save the model.
        obj.image.delete()