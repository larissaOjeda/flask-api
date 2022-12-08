# To be able to use env vars
from decouple import config 

class Config:
    SECRET_KEY=config('SECRET_KEY')

# to refresh server automatically when changes occur
class DevelopmentConfig(Config): 
    DEBUG = True

config = {
    'development': DevelopmentConfig
}