from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from busstops import views

router = routers.DefaultRouter()
router.register(r'busstops', views.BusStopsView, 'busstops')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
