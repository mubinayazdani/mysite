from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Category, Product, File 

# Register your models here.



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent','title','description','created_time']
    list_filter = ['title','parent']
    search_fields = ['title']

class FileInLineAdmin(admin.TabularInline):
    model = File
    fields = ['title','file_type','file','is_enable']
    extra = 0

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['title','created_time']
    list_filter = ['title']
    filter_horizontal =['categories']
    inlines = [FileInLineAdmin]