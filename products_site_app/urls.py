from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name='products_site_app'
urlpatterns = [
    path("", views.index, name="index"),
    path("cart/", views.cart, name="cart"),
    path("search/", views.search, name="search"),
    path("search/<slug:sort_by>/", views.search, name="search"),
    path("search/<slug:sort_by>/<slug:search>/", views.search, name="search"),
    path("details/<int:id>/", views.details, name="details"),
    path('added_item/', views.added_item, name="added_item"),
    path('products/form/', views.products_form, name="products_form"),
    path('product/created/', views.product_created, name="product_created"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)