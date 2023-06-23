import os
from decouple import config
from dotenv import load_dotenv
from datetime import timedelta
from pymongo import MongoClient

BASE_DIR=os.path.dirname(os.path.realpath(__file__))
load_dotenv()

class Config:
    SECRET_KEY=config('SECRET_KEY', 'secret')
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(minutes=30)
    JWT_SECRET_KEY=config('JWT_SECRET_KEY', 'secret')
    MONGO_URI = os.getenv('MONGODB_PROD_URI')
    DB_NAME = os.getenv('DB_NAME')

class DevConfig(Config):
    DEBUG=config('DEBUG', cast=bool)
    MONGO_URI = os.getenv('MONGODB_DEV_URI')
    DB_NAME = os.getenv('DB_NAME_DEV','kilega_dev')
    


class TestConfig(Config):
    TESTING=True
    

class ProdConfig(Config):
    pass

config_dict = {
    'development': DevConfig,
    'production': ProdConfig,
    'testing': TestConfig
}

enviroment = os.getenv("ENV", "development")
app_configuration = config_dict[enviroment]
def connect_mongo(tenant):
    client = MongoClient(app_configuration.MONGO_URI)
    db = client[f"{app_configuration.DB_NAME}_{tenant.lower()}"]
    return db