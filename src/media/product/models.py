from tkinter import CASCADE
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    PRDName=models.CharField(max_length=400, verbose_name=_(" Name"))
    PRDModel=models.CharField(max_length=400, verbose_name=_(" Model"))
    PRDImage=models.ImageField(upload_to='productimage/', verbose_name=_("Prduct Image"),blank=True, null=True)
    PRDCatrgory=models.ForeignKey( 'Category', related_name='categories', verbose_name=_("Category"), on_delete=models.CASCADE,blank=True, null=True)
    PRDBrand=models.ForeignKey('settings.Brand', verbose_name=_("Brand"),on_delete=models.CASCADE,blank=True, null=True)
    PRDDesc=models.TextField(verbose_name=_("Product Description"))
    PRDPrice=models.DecimalField(max_digits=12,decimal_places=4,verbose_name=_("Price"))
    PRDDiscount=models.DecimalField(max_digits=8,decimal_places=4,verbose_name=_("Discount Price"))
    PRDCost=models.DecimalField(max_digits=12,decimal_places=4 ,verbose_name=_("Cost"))
    PRDCreated=models.DateTimeField(verbose_name=_("Created At"))
    PRDStyle=models.ForeignKey('Style', verbose_name=_("Style"), on_delete=models.CASCADE,blank=True, null=True)
    PRDSlug=models.SlugField(blank=True,null=True,verbose_name=_("Product URL"))
    PRDISNew=models.BooleanField(default=True,verbose_name=_("New Product"))
    PRDISBestseller=models.BooleanField(default=False,verbose_name=_("Best Seller"))
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    
    class meta :
        verbose_name=_("Product ")
        verbose_name_plural=("Products")
        
        
    def save (self, *args, **kwargs):
        if not self.PRDSlug :
            self.PRDSlug=slugify(self.PRDName)
        super(Product , self).save(*args,**kwargs)
        
    
        
    
    def __str__(self):
        return self.PRDName
    
class ProductImage (models.Model):
    PRDIProduct=models.ForeignKey(Product ,on_delete=models.CASCADE ,verbose_name=_("Product Name"))
    PRDIImage=models.ImageField(upload_to='productimage/',verbose_name=_("Image"))
    
    def __str__(self):
        return str(self.PRDIProduct )
    
class Category (models.Model):
    CATName=models.CharField(max_length=50,verbose_name=_("Name"))
    CATParent=models.ForeignKey('self',on_delete=models.CASCADE,limit_choices_to={'CATParent__isnull': True},verbose_name=_("Main Category"),blank=True,null=True)
    CATDesc=models.TextField(verbose_name=_("Description"),blank=True, null=True)
    CATImg=models.ImageField(upload_to='category/',verbose_name=_("Image"),blank=True, null=True)
    CATBrand=models.ForeignKey('settings.Brand', verbose_name=_("Brand"),on_delete=models.CASCADE,blank=True, null=True)
    slug=models.SlugField(blank=True,null=True,verbose_name=_("Category URL"))
    
    
    class meta :
        verbose_name=_("Category")
        verbose_name_plural=_("Categories")
             
    def save (self, *args, **kwargs):
        if not self.slug :
            self.slug=slugify(self.CATName)
        super(Category , self).save(*args,**kwargs)
    def __str__(self):
        return str(self.CATName)
        
class Style (models.Model):
    STYName=models.CharField(max_length=50,verbose_name=_("Name")) 
    STYImg=models.ImageField(upload_to='category/',verbose_name=_("Image"),blank=True, null=True)
    class meta :
        verbose_name=_("Style")
        verbose_name_plural=_("Styles")
    def __str__(self):
        return str(self.STYName)
        
        
        
        
class Product_Alternative(models.Model):   
    PALNProduct=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='main_product',verbose_name=_("Product"))
    PALNAlternatives=models.ManyToManyField(Product,related_name='alternatives_product',verbose_name=_("Alternatives"))
    class meta :
        verbose_name=_("Product Alternative")
        verbose_name_plural=_("Product Alternatives")
    def __str__(self):
        return str(self.PALNProduct)
    
class Product_accessories(models.Model):
    PACCProduct=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='mainaccessories_product',verbose_name=_("Product"))
    PACCAccessories=models.ManyToManyField(Product,related_name='accessories_product',verbose_name=_("Accessories"))
    class meta :
        verbose_name=_("Product Accessory")
        verbose_name_plural=_("Product Accessories")
    def __str__(self):
        return str(self.PACCProduct)    
        
RATE_CHOICES = [
(1,"Terrible"),
(2,"Bad"),
(3,'Not Bad'),
(4,"Good"),
(5,"Very Good")]   


class Review(models.Model):
    comment=models.TextField(max_length=500,verbose_name='Comment',null=True,blank=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=_("User Nme"),default='User')  
    product_REV=models.ForeignKey(Product,related_name='review',verbose_name=_("Product Reviews"),on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    rate=models.PositiveSmallIntegerField(choices=RATE_CHOICES ,blank=True, null=True)
    likes=models.PositiveSmallIntegerField(default=0)
    unlikes=models.PositiveSmallIntegerField(default=0)
    
    class meta :
        verbose_name=_("Product Review")
        verbose_name_plural=_("Product Reviews")
    
    def __str__(self):
        return str(self.created_by)
        
        
        
class ContactUs(models.Model):  
    place=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=20)
    email=models.EmailField(max_length=254)
    


    class meta :
            verbose_name=_("ContactUs")
            verbose_name_plural=_("ContactUs")
     
    def __str__(self):
        return self.email
    
    