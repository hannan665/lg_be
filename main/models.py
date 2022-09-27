from django.db import models


# Create your models here.

def upload_to(inctance, filename):
    return 'images/{filename}'.format(filename=filename)


class ColorTone(models.Model):
    title = models.CharField(max_length=512)
    code = models.CharField(max_length=512)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Color Tones"


class Industry(models.Model):
    title = models.CharField(max_length=512)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Industries"


class TypeAndPreferences(models.Model):
    title = models.CharField(max_length=512)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Type and Preferences"


class Logo(models.Model):
    business_name = models.CharField(max_length=512)
    email = models.EmailField()
    user_name = models.CharField(max_length=512)
    slogan = models.CharField(max_length=512)
    industry = models.ManyToManyField(Industry)
    color_tone = models.ManyToManyField(ColorTone)
    type_and_preferences = models.ManyToManyField(TypeAndPreferences)

    def __str__(self):
        return f'{self.business_name} - {self.email}'

    class Meta:
        verbose_name_plural = "Logos"


class SubProduct(models.Model):
    price = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=512)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Sub products"

class Services(models.Model):
    title = models.CharField(max_length=512)
    sub_product = models.ForeignKey(SubProduct, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Services"


class Product(models.Model):
    price = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=512)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    sub_products = models.ManyToManyField(SubProduct)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Products"
