from django.core.exceptions import ValidationError

def validate_title_case(value):
    if not value.istitle():
        raise ValidationError("Subject must be in title case format.")
    
def validate_professor_name(value):
    if not value.startswith('Professor '):
        raise ValidationError('Professor name must be in the format "Professor Adam".')