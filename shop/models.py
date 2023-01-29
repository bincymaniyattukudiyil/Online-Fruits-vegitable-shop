from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(max_length=150,unique=True)
    cat_img=models.ImageField(upload_to='images')
    class meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def __str__(self):
       return '{}'.format(self.name)
    def slugget(self):
        return reverse('prod_cat',args=[self.slug])
class Items(models.Model):
    Item_name=models.CharField(max_length=150)
    Item_slug=models.SlugField(max_length=150,unique=True)
    Item_cat=models.ForeignKey(category,on_delete=models.CASCADE)
    Item_desc=models.TextField()
    Item_price=models.IntegerField()
    Item_stock=models.IntegerField()
    available=models.BooleanField(default=True)
    Item_img=models.ImageField(upload_to='images')
    def __str__(self):
        return '{}'.format(self.Item_name)

    def get_url1(self):
        return reverse('details',args=[self.Item_slug])
class Cart(models.Model):
    Item_id=models.ForeignKey(Items,on_delete=models.CASCADE)
    c_qty=models.IntegerField()
    c_date=models.DateTimeField(auto_now_add=True)
    C_id=models.CharField(max_length=4)

    def __str__(self):
        return '{}'.format(self.Item_id)
    def Total(self):
        return self.Item_id.Item_price*self.c_qty

class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.TextField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    Contact = models.IntegerField()
