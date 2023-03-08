from dotenv import load_dotenv
load_dotenv()
import os

class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:vipascal@localhost:5432/canvasdb'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TSL = False
    MAIL_USE_SSL = True
    MAIL_DEBUG = False
    MAIL_DEFAULT_SENDER = 'noreply@flask.com'
    SECURITY_PASSWORD_SALT = 'base64code'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME') 
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

