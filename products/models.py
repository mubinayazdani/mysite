from django.db import models

from django.utils.translation import gettext_lazy as _ 
# Create your models here.


class Category(models.Model):
    
    
    parent = models.ForeignKey('self', verbose_name = _('parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length = 50)
    description = models.TextField(_('Description'))
    avatar = models.ImageField(_('Avatar'), blank=True, upload_to='categories/')
    is_enable = models.BooleanField(_('Is_enable'), default=True)
    created_time = models.DateTimeField(_('Created_time'), auto_now_add = True)
    updated_time = models.DateTimeField(_('Updated_time'), auto_now_add = True)
    
    
    class Meta:
        
        db_table = _('categories')
        verbose_name = _('Category')
        verbose_name_plural = _('categories')
        
        
    def __str__(self):
        
        return f'{self.title}'



class Product(models.Model):
    
    title = models.CharField(_('Title'), max_length = 50)
    description = models.TextField(_('Description'))
    avatar = models.ImageField(_('Avatar'), blank=True, upload_to='products/')
    categories = models.ManyToManyField(Category, verbose_name=_('categories'), blank=True)
    created_time = models.DateTimeField(_('Created_time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('Updated_time'),auto_now_add=True)
    
    
    class Meta:
        
        db_table = _('products')
        verbose_name = _('Product')
        verbose_name_plural = _('products')

    def __str__(self):
        
        return f'{self.title}'

class File(models.Model):
    
    
        
        FILE_AUDIO = 1
        FILE_VIDEO = 2
        FILE_PICTURE = 3
        FILE_TYPES=(
            
            (FILE_AUDIO , _('Audio')),
            (FILE_VIDEO , _('Video')),
            (FILE_PICTURE , _('Picture')),
            
        )
    
    
    
        products = models.ForeignKey(Product, verbose_name=_('product'), related_name='files',on_delete=models.CASCADE)
        title = models.CharField(_('Title'), max_length = 50)
        is_enable = models.BooleanField(_('Is_enable'), default=True)
        file_type = models.PositiveSmallIntegerField(_('File_type'), choices = FILE_TYPES, default = FILE_PICTURE)
        file = models.FileField(_('File'), upload_to=('files/%y/%m/%d'))
        created_time = models.DateTimeField(_('Created_time'), auto_now_add = True)
        updated_time = models.DateTimeField(_('Updated_time'), auto_now_add = True)
        
        
        class Meta:
            
            db_table = _('files')
            verbose_name = _('File')
            verbose_name_plural = _('files')


        def __str__(self):
            
            return f'{self.title}'