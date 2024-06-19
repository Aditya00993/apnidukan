from django.db import models



class All(models.Model):
    productid = models.AutoField
    desc = models.CharField(max_length=300)
    subcategory = models.CharField(max_length=50,default='')
    publish = models.DateField()  
    price = models.IntegerField(default=0) 
    image  =models.ImageField(upload_to= 'shop',default='')

 

class Ram(models.Model):

    productid = models.AutoField
    product_name = models.CharField(max_length=25,default='')
    desc = models.CharField(max_length=300)
    category = models.CharField(max_length=30,default='')
    subcategory = models.CharField(max_length=50,default='')
    publish = models.DateField()  
    price = models.IntegerField(default=0) 
    image  =models.ImageField(upload_to= 'shop',default='')

def __str__(self):
     return self.product_name



class Con(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    message = models.CharField(max_length=350)
   
def __str__(self):
     return self.name




   
   