from django.shortcuts import render, redirect
from .models import Products, Cart_products
from .forms import Products_form
from django.http import JsonResponse
import json
import time
from decimal import Decimal

# Create your views here.
def index(request):
    products = Products.objects.all()
    return render(request, "index.html", {"products":products})



def cart(request):
    cart = Cart_products.objects.all()
    subtotal = 0
    shipping = Decimal("4.90")
    total_cart = 0
    
    for i in cart:
        subtotal+=(i.price*i.quantity)
        total_cart+=i.quantity
    total = subtotal + shipping
    
    return render(request, "cart.html", {"cart":cart, 
                                         "subtotal":subtotal, 
                                         "shipping":shipping, 
                                         "total":total,
                                         "total_cart":total_cart,
                                        })



def search(request, sort_by="", search="empty"):
    if request.POST:
        search = request.POST['search_by']
        products_name= dict()
        products_id= dict()
    
        if search:
            if search.isnumeric():
                """If user look for id number we load the details view"""
                print("got in id")
                details = Products.objects.get(id=search)
                return render(request, "details.html", { 'details':details})
            else:
                """Function looks for products based on name and filter it """
                if sort_by == "":
                    products_name = Products.objects.filter(name__istartswith=search)
                else:
                    products_name = Products.objects.filter(name__istartswith=search).order_by(sort_by)
        else:
            search="empty"#search value can not be blank
            products_name = Products.objects.all()#If search field is blank show all

        
        return render(request, "search.html", {'products_name':products_name, "search":search})

    if search == "empty" and sort_by == "":
        products_name = Products.objects.all()
    elif search == "empty" and sort_by != "":
        products_name = Products.objects.all().order_by(sort_by)
    elif search != "empty" and sort_by == "":
        products_name = Products.objects.filter(name__istartswith=search)
    elif search != "empty" and sort_by != "":
        products_name = Products.objects.filter(name__istartswith=search).order_by(sort_by)
    
    

    return render(request, "search.html",{'products_name':products_name, "sort_by":sort_by, "search":search})
    



def details(request, id):
    details = Products.objects.get(id=id)
    return render(request, "details.html", {"details":details})



def added_item(request):
    #For adding and removing from cart functions
    if request.GET.get('id'):
    
        productId = request.GET.get('id')
        action = request.GET.get('action')
    
    
        print("id: ", productId)
        print("action:",action)
    
        product = Products.objects.get(id=productId)
        order_product, created = Cart_products.objects.get_or_create(
            product_id_id=product.id, 
            name=product.name, 
            description=product.description, 
            picture=product.picture, 
            price=product.price
            )
    
        if action == 'add':
            order_product.quantity += 1
        elif action == "remove":
            order_product.quantity -= 1
        order_product.save()
        if order_product.quantity == 0:
            order_product.delete()
        
        return JsonResponse('item was added', safe=False)

    #for Sorting function
    elif request.GET.get('sort'):
        sort_by = request.GET.get('sort')
        
        if sort_by == "name":
            products = Products.objects.order_by(sort_by)
        else:
            products = Products.objects.order_by("price")
        if sort_by == "price_high":
            products = Products.objects.order_by("-price")

        products = [ products_serializer(product) for product in products ]
        
        return JsonResponse(products, safe=False)

    # for Finding function
    elif request.GET.get('search'):
        search = request.GET.get('search')
        sort_by = request.GET.get('sort')
        print(sort_by)
        print("type:", type(search), search)
        products_name= dict()
        products_id= dict()
        
        if search:
            if search.isnumeric():
                print("got in id")
                details = Products.objects.get(id=search)
                return render(request, "details.html", { 'details':details })


        else:
            print("got in name")
            if sort_by == "name":
                products_name = Products.objects.filter(name__istartswith=search).order_by("name")
            elif sort_by == "price":
                products_name = Products.objects.filter(name__istartswith=search).order_by("price")
            elif sort_by:
                products_name = Products.objects.filter(name__istartswith=search)
        # return render(request, "search.html", {'products_name':products_name})
    
        # return render(request, "search.html",{'new_search':True})
        return JsonResponse('Searching', safe=False)

def products_form(request):
    """It appears when an admin is logged in"""
    if request.method=="POST":
        form=Products_form(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            # form.name = request.POST["name"]
            # form.description = request.POST["description"]
            # form.price = request.POST["price"]
            # form.picture = request.POST["picture"]
            return redirect("/product/created/")
            

    form = Products_form()
    return render(request, "products_form.html", {"form":form})

def product_created(request):
    return render(request, "product_created.html")
def products_serializer(product):
    """Function to convert into dict the products object so json can handle it"""
    return{'id': product.id, 
        'name': product.name, 
        'description': product.description,
        'price': product.price,
        'picture': str(product.picture)
        }

