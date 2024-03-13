import random

from django.contrib.auth.models import User 
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, send_mail



class UserManager(BaseUserManager):
    
    use_in_migration = True
    
    def _create_user(self, username, phone_number, email, password, is_staff, is_superuser, **extra_fields):
        
        now = timezone.now 
        
        if not username:
            raise ValueError('The given username must be set!')
        
        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number,
                          username=username,
                          email=email,
                          is_staff=is_staff,
                          is_active=True,
                          is_superuser=is_superuser,
                          **extra_fields)
        
        if not extra_fields.get('no_password'):
            user.set_password(password)
            
            
        user.save(using=self._db)
        return user
    
    def create_user(self, username=None, phone_number=None, email=None, password=None, **extra_fields):
        if username is None:
            if email:
                username = email.split('@',1)[0]
            if phone_number:
                username = random.choice('abcdefghijklmnopqrstuvwxyz') + str(phone_number)[-7:]
            
            while User.objects.filter(username=username).exists():
                username += str(random.randint(10,99))
                
        return self._create_user(username, phone_number, email, password, False, False, **extra_fields)
    
        
     
    def create_superuser(self, username, phone_number, email, password, **extra_fields):
        return self._create_user(username, phone_number, email, password, True, True, **extra_fields )
    
    
    def get_by_phone_number(self, phone_number):
        return self.get(**{'phone_number':phone_number})
    
    def __str__(self):
        return str('class.__name__')
    
    
    
    


class User(AbstractBaseUser,PermissionsMixin):
    
    username = models.CharField(_('Username'), max_length=15,unique=True,
                                help_text=_(
                                    'Required 15 characters or fewer starting with a letter! '
                                ),

                                validators = [
                                    validators.RegexValidator(r'^[a-zA-z][a-zA-Z0-9_\.]+$',_('Enter a valid username.'), 'this may contains letterrs', 'invalid')])
    
    first_name = models.CharField(_('First name'), max_length=30,blank=True)
    last_name = models.CharField(_('Last name'), max_length=30,blank=True)
    email = models.EmailField(_('Email adress'),unique=True, null=True,blank=True)
    phone_number = models.BigIntegerField(_('Mobile number'),unique=True,null=True,blank=True,
                                          validators=[
                                              validators.RegexValidator(r'^989[0-3,9]\d{8}$',
                                                                        ('Enter a valid mobiile number!'))
                                          ])
    is_staff = models.BooleanField(_('Is staff'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site. '))
    is_active = models.BooleanField(_('Active'), default=True,
                                    help_text=_('Designates whether this user should be treated as active'))
    
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number','email']
    
    
    class Meta:
        
        db_table = 'users'
        verbose_name = _('user')
        verbose_name_plural = _('users')
        
    
    def get_full_name(self):
        
        full_name = '%s %s' % (self.first_name,self.last_name)
        return full_name.strip()
        
    def get_short_name(self):
        
        return self.first_name
    
    def emailuser(self, subject, message, from_email=None, **kwargs):
        
        send_mail(subject, message, from_email, [self.email], **kwargs)
        
    @property
    def is_loggedin_user(self):
        return self.phone_number is not None or self.email is not None
    
    
    
    
    
class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField(_('Nick name'), max_length=50,blank=True)
    avatar = models.ImageField(_('Image Fields'), blank=True)
    bithday = models.DateField(_('Birthday'),null=True,blank=True)
    gender = models.BooleanField(_('Gender'),null=True,help_text=_('female is false, male is true, null is unset.'))
    provience = models.ForeignKey(verbose_name=_('Province'),to='Province',null=True,on_delete=models.SET_NULL)
    
    
    
    class Meta:
        
        db_table = 'user_profiles'
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')
        
        
    @property
    def get_first_name(self):
        return self.user.first_name
    
    @property
    def get_last_name(self):
        return self.user.last_name
    
    @property
    def get_nickname(self):
        return self.nick_name if self.nick_name else self.user.username
    
    
    def __str__(self):
        return str('class.__name__')
    
    
class Device(models.Model):
    
    WEB = 1
    IOS = 2
    ANDROID = 3
    
    DEVICE_TYPE_CHOCES = (
        
        (WEB,'web'),
        (IOS,'ios'),
        (ANDROID,'android')
    )
    
    user = models.ForeignKey(User, related_name='deevices',on_delete=models.CASCADE)
    device_uuid = models.UUIDField(_('Device UUID'),null=True )
    device_type = models.PositiveSmallIntegerField(choices=DEVICE_TYPE_CHOCES,default=ANDROID)
    device_os = models.CharField(_('Device os'), max_length=50,blank=True )
    device_model = models.CharField(_('Device model'), max_length=50,blank=True)
    app_version = models.CharField(_('App version'), max_length=50,blank=True)
    
    
    
    class Meta:
        
        db_table = 'user_devices'
        verbose_name = _('device')
        verbose_name_plural = _('devices')
        
        
        
class Province(models.Model):
    
    
    name = models.CharField(max_length=50)
    is_valid = models.BooleanField(default=True)
    # modified_at = models.DateTimeField(auto_now_add=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        
        return f'{self.name}'
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    