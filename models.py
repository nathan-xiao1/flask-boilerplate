from flask_login import UserMixin

class User(UserMixin):
    
    def __init__(self, username=None, password=None):
        self._username = name
        self._password = password
        
    @property
    def id(self):
        return self._username