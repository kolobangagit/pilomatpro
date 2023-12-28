from django.urls import path
from .views import Index, LocationDetailVIew, CityDetailView, CategoryDetailView, LocationAllPrice
from .utils import send_bot_info

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('location/<slug:slug>/', LocationDetailVIew.as_view(), 
          name='location_detail'),
    path('location/<slug:slug>/<slug:slug_city>/', CityDetailView.as_view(), 
          name='location_city'),
    path('location/<slug:slug>/product/<slug:slug_category>/', CategoryDetailView.as_view(), 
          name='location_category'),
    path('cites/<slug:slug_city>/<slug:slug_category>/', CategoryDetailView.as_view(), 
          name='location_city_product'),
    path('<slug:slug>/cena-pilomateriala/', LocationAllPrice.as_view(), name="location_all_price"),  
    path('send-info/', send_bot_info, name="send_bot_info"),
]
