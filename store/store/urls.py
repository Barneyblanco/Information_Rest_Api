
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from information import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorys/', views.categoryList.as_view()),
    path('sellers/', views.sellerList.as_view()),
    path('products/', views.productList.as_view()),
    path('orders/', views.orderList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)