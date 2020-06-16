from django.urls import path
from . import views
### Is this temporary code for debug mode? May not be in the right urls.py
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home-page'),
    path('products/<str:pk_prod>/', views.product, name='products-home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
We could add dynamic links to products here. e.g. /products/id=213

'''