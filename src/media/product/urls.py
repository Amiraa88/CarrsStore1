from django.urls import path
from . import views
app_name ='product'

urlpatterns = [
    path('',views.home,name='home'), 
    path('product/',views.product_list,name='product_list'),
    path('product/category',views.category_list,name='category_list'),
    path('category/<slug:slug>',views.categoryView,name='categoryView'),
    path('product/<slug:slug>',views.product_detail,name='product_detail'),
 
]