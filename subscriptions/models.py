from django.db import models
from django.utils.translation import gettext_lazy as _ 

from users.models import User 

from utils.validators import validate_SKUValidator
# Create your models here.


class Package(models.Model):
    
    title = models.CharField(_('Title'), max_length=50)
    sku = models.CharField(_('Stock keeping unit'), max_length=50, validators=[validate_SKUValidator])
    description = models.TextField(_('Description'), blank=True)
    avatar = models.ImageField(_('Avatar'), blank=True, upload_to='packages/')
    is_enable = models.BooleanField(_('Is enable'), default=True)
    price = models.PositiveIntegerField(_('Price'))
    duration = models.DurationField(_('Duration'), blank=True, null=True)
    # gateways = models.ManyToManyField('payments.Gateway')
    created_time = models.DateTimeField(_('Created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('Updated time'), auto_now_add=True)
    
    
    class Meta:
        
        db_table = 'packages'
        verbose_name = _('Package')
        verbose_name_plural = _('Packages')
        
    
    def __str__(self):
        
        return f'{self.title}'
      
        
        

class Subscription(models.Model):
    
    user = models.ForeignKey('users.User', related_name='%(class)s', on_delete=models.CASCADE)
    package = models.ForeignKey(Package, related_name='%(class)s', on_delete=models.CASCADE)
    created_time = models.DateTimeField(_('Created time'), auto_now_add=True)
    expire_time = models.DateTimeField(_('Expire time'), blank=True, null=True)
    
    
    class Meta:
        
        db_table = 'subscriptions'
        verbose_name = _('Subscription')
        verbose_name_plural = _('Subscriptions')