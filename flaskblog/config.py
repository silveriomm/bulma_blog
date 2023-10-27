import os
 
BASE_DIR = os.path.dirname(os.path.abspath(__name__)) 

class Config:
    SECRET_KEY = 'a1c8d3c9fef78b458f2a5312b2ff4966'
    SQLALCHEMY_DATABASE_URI= 'sqlite:///' + os.path.join(BASE_DIR, 'database.sqlite')
    MAIL_SERVER= 'smtp.ethereal.email'
    MAIL_PORT= 587
    # MAIL_USERNAME= os.environ.get('EMAIL_USER')
    # MAIL_PASS = os.environ.get('EMAIL_PASS')
    MAIL_USERNAME = 'rebekah.wintheiser46@ethereal.email'
    MAIL_PASSWORD = 'e6fvmSSa7ZuaASWPXX'
    MAIL_USE_TLS = True


