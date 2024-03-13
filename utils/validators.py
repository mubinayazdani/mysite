from django.core.validators import RegexValidator 
from django.utils.translation import gettext_lazy as _ 

class PhoneNumberValidator(RegexValidator):
    
    regex = '^98(9[0-3,9]\d{8}|[1-9]\d{9})$'
    message = 'Phone number must be a VALID 12 digits like 98xxxxxxxxxx.'
    code = 'Invalid_phone_number'
    
    
    
class SKUValidator(RegexValidator):
    
    regex = '^[a-zA-Z0-9\-\_]{6,20}$'
    message = 'SKU must be a alphanumeric with 6 to 20 characters.'
    code = 'Invalidate_sku'
    
    
    
class UsernameValidator(RegexValidator):
    
    regex = '^[a-zA-Z][a-zA-Z0-9_\.]+$'
    message = _('Enter a valid username starting with a-z.')
    code = 'Invalid_username'
    
    
    
class PostalCodeValidator(RegexValidator):
    
    regex = '^[0-9]{10}$'
    message = _('Enter a valid postal code.')
    code = 'Invalid_postal_card'
    
    
    
class IDNumberValidator(RegexValidator):
    
    regex = '^[0-9]{10}$'
    message = _('Enter a valid id number.')
    code = 'Invalid_id_number'
    
    
    
class IBanNumberValidator(RegexValidator):
    
    regex = '^[a-zA-Z]{2}[0-9]{2}[a-zA-Z0-9]{4}[0-9]{7}([a-zAZ0-9]?){0,16}$'
    message = _('Enter a valid iban number.')
    code = 'Invalid_bank_card_number'
    
    
    
class BankCardNumberValidator(RegexValidator):
    
    regex = '^[0-9]{16}$'
    message = _('Enter a valid card number.')
    code = 'Invalid_bank_card_number'
    
    
    
validate_phone_number = PhoneNumberValidator()
validate_SKUValidator = SKUValidator()
username_validator = UsernameValidator()
postalcard_validator = PostalCodeValidator()
idnnumber_validator = IDNumberValidator()
ibannumber_validator = IBanNumberValidator()
bankcard_validator = BankCardNumberValidator()
    
    
    
