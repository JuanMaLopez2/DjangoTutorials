from django.urls import path 

from .views import HomePageView, AboutPageView, ProductIndexView, ProductShowView, ProductCreateView, ContactView, ProductListView, CartView,CartRemoveAllView
 

urlpatterns = [ 

    path("", HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductIndexView.as_view(), name='index'), 
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('products/', ProductListView.as_view, name='products'),
    path('cart/', CartView.as_view(), name='cart_index'), 
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'), 
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'), 
] 