from django.contrib import admin

from .models import Category, Sub_Category, Slider, Service


admin.site.register(Slider)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Sub_Category)
