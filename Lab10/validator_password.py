from re import *
from validator import Validator
from register_form_fields import RegisterFormFields

class PasswordValidator(Validator):
    def __init__(self, password):
        self.password = password

    def is_valid(self):
        if self.password is None or len(self.password) < 4:
            return False
        regex = r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-]).{4,}$"
        return bool(match(regex, self.password))

    def field_name(self):
        return RegisterFormFields.PASSWORD
