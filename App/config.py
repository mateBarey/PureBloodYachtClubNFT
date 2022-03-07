import os


class Config(object):
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')
    MONGO_DATABASE_URI = os.environ.get("DATABASE_URL")
    SECRET_KEY = os.environ.get("secret_key")