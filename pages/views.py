from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView 
from django.views import View
from django import forms
from django.urls import reverse

# Create your views here.

class HomePageView(TemplateView): 
     template_name = 'pages/home.html'

class AboutPageView(TemplateView): 
    template_name = 'pages/about.html' 


    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({ 
            "title": "About us - Online Store", 
            "subtitle": "About us", 
            "description": "This is an about page ...", 
            "author": "Developed by: Your Name", 
        }) 

        return context 
    
class Product(View): 
    products = [ 
        {"id":"1", "name":"TV", "description":"Best TV","price":999}, 
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":1200}, 
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price":15}, 
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price":99} 
    ] 

class ProductIndexView(View): 
    template_name = 'products/index.html' 

    def get(self, request): 
        viewData = {} 
        viewData["title"] = "Products - Online Store" 
        viewData["subtitle"] =  "List of products" 
        viewData["products"] = Product.products 

        return render(request, self.template_name, viewData) 

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        viewData = {}

        try:
            product = Product.products[int(id) - 1]

            viewData["title"] = product["name"] + " - Online Store"

            viewData["subtitle"] = product["name"] + " - Product information"

            viewData["product"] = product

            return render(request, self.template_name, viewData)
        except IndexError:
            return HttpResponseRedirect(reverse('home'))
    
class ProductForm(forms.Form): 
    name = forms.CharField(required=True) 
    price = forms.FloatField(required=True) 

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("Price cannot be negative")
        return price

class ProductCreateView(View): 
    template_name = 'products/create.html' 

    def get(self, request): 
        form = ProductForm() 
        viewData = {} 
        viewData["title"] = "Create product" 
        viewData["form"] = form 
        return render(request, self.template_name, viewData) 
   
    def post(self, request): 
        form = ProductForm(request.POST) 
        if form.is_valid(): 
            return render(request, 'products/product_created.html')

        else:
            viewData = {} 
            viewData["title"] = "Create product" 
            viewData["form"] = form 
            
            return render(request, self.template_name, viewData)

class ContactView(TemplateView):        
    template_name = 'pages/contact.html'