from django.db import models 
from django.utils.translation import gettext_lazy as _

from utils.validators import validate_phone_number

# Create your models here.


class Gateway(models.Model):
    
    title = models.CharField(_('Title'), max_length=50)
    description = models.TextField(_('Description'),blank=True)
    avatar = models.ImageField(_('Avatar'), blank=True, upload_to='gateways/')
    is_enable = models.BooleanField(_('Is enable'), default=True)
    created_time = models.DateTimeField(_('Created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('Updated time'), auto_now_add=True)
    
    
    
    class Meta:
        
        db_table = 'gatewys'
        verbose_name = 'Gateway'
        verbose_name_plural = 'Gateways'
        
        


class Payment(models.Model):
    
    STATUS_VOID = 0
    STATUS_PAID = 10
    STATUS_ERROR = 20
    STATUS_CANCELED = 30
    STATUS_REFUNDED = 1
    STATUS_CHOICES = (
        (STATUS_VOID, _('Void')),
        (STATUS_PAID, _('Paid')),
        (STATUS_ERROR, _('Error')),
        (STATUS_CANCELED, _('User Canceled')),
        (STATUS_REFUNDED, _('Refunded'))
    
    )
    
    STATUS_TRANSLATION = {
        
        STATUS_VOID : _('Payment could not be proccessed.'),
        STATUS_PAID : _('Payment successful.'),
        STATUS_ERROR : _('Payment has encountered an error.'),
        STATUS_CANCELED : _('Payment canceled by user.'),
        STATUS_REFUNDED : _('This payment has been refunded.')
        
    }
    
    
    user = models.ForeignKey('users.User', verbose_name=_('user'), related_name='%(class)s', on_delete=models.CASCADE)
    package = models.ForeignKey('subscriptions.Package', verbose_name=_('package'), related_name='%(class)s', on_delete=models.CASCADE)
    gateway = models.ForeignKey(Gateway, verbose_name=_('gateway'), related_name='%(class)s', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(_('Price'), default=0)
    status = models.PositiveSmallIntegerField(_('Status'), choices=STATUS_CHOICES, default=STATUS_VOID, db_index=True)
    device_uuid = models.CharField(_('Device uuid'), max_length=40, blank=True)
    token = models.CharField(_('Token'), max_length=10)
    phone_number = models.BigIntegerField(_('Phone number'), validators=[validate_phone_number], db_index=True)
    consumed_code = models.PositiveIntegerField(_('Consumed refrence code'), null=True, db_index=True)
    created_time = models.DateTimeField(_('Created time'), auto_now_add=True, db_index=True)
    updated_time = models.DateTimeField(_('Modification time'), auto_now_add=True)
    
    
    
    class Meta:
        
        db_table = 'payyments'
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')
        