# A class with the contents of the application configurations

class Config:
    SECRET = 'eedfgcasd123vbnhyth'
    SQLALCHEMY_DATABASE_URI = "sqlite:///movies.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}
    DEBUG = True
