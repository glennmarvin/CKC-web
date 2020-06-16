from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category, Services, Billboard, AboutUs
from itertools import chain
from django.utils.translation import LANGUAGE_SESSION_KEY, activate, get_language
import random


#https://docs.djangoproject.com/en/2.0/_modules/django/utils/translation/#activate for translation funcs

# we will use this as an example on how to pass on variables in JSON style
# we will get a similar response from our database model

# Create your views here.
def home(request):    
    if request.method == "POST":
        if request.POST.get('langupdate', False):
            language = request.POST['langupdate']
            print("if", language)
            request.session['lang'] = language
    elif 'lang' in request.session:
        language = request.session['lang']
        print("elif", language)
    else: 
        language = get_language()
        print("else", language)

    activate(language)

    return render(request, 'products/home.html', {'productinfo': Product.objects.all(), 'services': Services.objects.all(), 'bbs': Billboard.objects.all(), 'abus': AboutUs.objects.all()})

def product(request, pk_prod):

    #### There are some language issues.... Have to be resolved. Now it does not get the lang value from the template.

    if request.method == "POST":
        if request.POST.get('langupdate', False):
            language = request.POST['langupdate']
            print("if", language)
            request.session['lang'] = language
    elif 'lang' in request.session:
        language = request.session['lang']
        print("elif", language)
    else: 
        language = get_language()
        print("else", language)

    activate(language)

    products = Product.objects.get(id=pk_prod)
    ids = [i.id for i in Product.objects.exclude(id=pk_prod)]
    random.shuffle(ids)
    similar_products = [Product.objects.get(id=i) for i in ids]

    return render(request, 'products/products.html', {'productinfo': products, 'similar': similar_products, 'activatedlang': language})


'''
Can set a cookie using:
response.set_cookie('lang', value)

Can get the cookie using:
if 'lang' in request.COOKIES:
    language = request.COOKIES

Can get the session language using: /// We will not use sessions because we just store lang, nothing more
if 'lang' in request.session:
    session_language = request.session
'''