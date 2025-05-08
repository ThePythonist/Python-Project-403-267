from django.contrib import admin
from django.urls import path
from .views import indexview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', indexview),
    path('', indexview),
]
