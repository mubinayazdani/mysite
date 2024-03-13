from django.contrib import admin

from .models import Gateway, Payment

# Register your models here.


@admin.register(Gateway)
class GatewayAdmin(admin.ModelAdmin):
    
    list_display = ['title','is_enable']
    
    
    
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    
    list_display = ['user','package','gateway','price','status','phone_number']
    list_filter = ['status','gateway','package']
    search_fields = ['user__username','phone_number']