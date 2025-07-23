from django.core.exceptions import ValidationError
import re

def validate_name_format(name):
    error_message = 'Name must be in the format "First Middle Initial. Last"'

    regex = r'^[A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+$'

    good_name = re.match(regex,name)

    if good_name:
        return name
    else:
        raise ValidationError(error_message, params={'name':name})
    
def validate_school_email(email):
    error_message = 'Invalid school email format. Please use an email ending with "@school.com".'

    regex = r'.*@school\.com$'
    
    good_email = re.match(regex,email)

    if good_email:
        return email
    else:
        raise ValidationError(error_message, params={'email':email})
    
def validate_combination_format(combo):
    error_message = 'Combination must be in the format "12-12-12"'

    regex = r'^[\d]{2}-[\d]{2}-[\d]{2}$'

    good_combo = re.match(regex,combo)

    if good_combo:
        return combo
    else:
        raise ValidationError(error_message, params={'combo':combo})