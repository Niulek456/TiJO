from validator import Validator
from register_form_fields import RegisterFormFields

class LastNameValidator(Validator):
    def __init__(self, last_name):
        self.last_name = last_name

    def is_valid(self):
        return self.last_name is not None and len(self.last_name.strip()) > 0

    def field_name(self):
        return RegisterFormFields.LAST_NAME
