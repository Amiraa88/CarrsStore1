from multiprocessing import context
from re import search
from unicodedata import category
from django.shortcuts import redirect, render, HttpResponse ,get_object_or_404
from settings.models import Brand
from .models import Product,Review,ContactUs,Category,Style
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .filters import ProductFilter
# Create your views here.

def home (request):
       my_info=ContactUs.objects.first()
       return render(request, 'home.html',{'my_info':my_info})
       
       
def product_list(request):
    product_list=Product.objects.all()
    
    ##search 
    PRDDesc=None
    if 'search_name' in request.GET:
        PRDDesc=request.GET['search_name']
        if PRDDesc :
            product_list= product_list.filter(PRDDesc__icontains=PRDDesc)
                   
     ##filters
    myfilter=ProductFilter(request.GET,queryset=product_list)
    product_list=myfilter.qs
    brand_list=Brand.objects.all()
    
    ##paginator
    paginator = Paginator(product_list,4 ) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    
    context={'product_list':product_list,'myfilter':myfilter,'brand_list':brand_list}
    return render(request, 'Product/all_cars.html',context)

def category_list(request):
   category_list=Category.objects.all()
   style_list=Style.objects.all()
   
   context={'category_list':category_list,'style_list':style_list}
  
   return render(request, 'Product/category.html',context)
def categoryView(request,slug):
   #products=Category.objects.all()
   
    category_products=Category.objects.get(slug=slug)
       
    category_name=Category.objects.filter(slug=slug).first()
    context={'category_products':category_products,'category_name':category_name}
    return render(request, 'Product/collection.html',context)   
 
       
       
def product_detail(request,slug):
    product_detail=Product.objects.get(PRDSlug=slug)
    context={'product_detail':product_detail}
    
    if request.method=='POST':
        comment=request.POST['content-comment']
        
        
        user=User.objects.first()    
        
        newcomment=Review.objects.create(
        comment=comment,
        product_REV=product_detail,
        created_by=user,)
        classify(newcomment)
    return render(request, 'Product/car_detail.html',context)
    

    
