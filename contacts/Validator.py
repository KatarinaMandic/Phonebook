from exceptions.InvalidEmailError import InvalidEmailError
from exceptions.InvalidTelephoneError import InvalidTelephoneError
import re

class Validator:

    # static methods

    @staticmethod
    def check_email(email):
        pattern = re.compile(".+@+.+\.+.+")
        if pattern.match(email):
            return True
        else:
            raise InvalidEmailError()

    @staticmethod
    def check_telephone (telephone):
        pattern = re.compile('^\+\d{3}\s\d{2}\s\d{3}\s\d{3,4}$')
        if pattern.match(telephone):
            return True
        else:
            raise InvalidTelephoneError()
