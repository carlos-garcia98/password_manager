class User:
    
    def __init__(self, id_account=None, app_name=None, username=None, password=None, url=None):
        self._id_account = id_account
        self._app_name = app_name
        self._username = username
        self._password = password
        self._url = url
    
    @property
    def id_account(self):
        return self._id_account
    
    @id_account.setter
    def id_account(self, id_account):
        self._id_account = id_account
    
    @property
    def app_name(self):
        return self._app_name
    
    @app_name.setter
    def app_name(self, app_name):
        self._app_name = app_name
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        self._username = username
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password
    
    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, url):
        self._url = url
    
    def __str__(self):
        return f'Account ID: {self._id_account}, App Name: {self._app_name}, Username: {self._username}, Password: {self._password}, URL: {self._url}'