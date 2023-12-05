from django.urls import path
from .views import ListCreateMenu, RetrieveUpdateDestroyMenu,CreateItem,ListCart

urlpatterns = [
    path("menu/", ListCreateMenu.as_view()),
    path("<int:pk>/menu/", RetrieveUpdateDestroyMenu.as_view()),
    path("item/", CreateItem.as_view()),
    path("<int:pk>/cart/",ListCart.as_view())
]
