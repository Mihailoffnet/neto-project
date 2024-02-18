from django.test import TestCase

# Create your tests here.

import os
from dotenv import load_dotenv
load_dotenv()

DEBUG = bool(os.getenv("DEBUG"))
SECRET_KEY = os.getenv('SECRET_KEY', '=hs6$#5om031nujz4staql9mbuste=!dc^6)4opsjq!vvjxzj@')
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", ['*']).split()

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))
EMAIL_USE_TLS = bool(os.getenv("EMAIL_USE_TLS"))
EMAIL_USE_SSL = bool(os.getenv("EMAIL_USE_SSL"))
SERVER_EMAIL = os.getenv("SERVER_EMAIL")


print(type(DEBUG), DEBUG)
print(type(SECRET_KEY), SECRET_KEY)
print(type(ALLOWED_HOSTS), ALLOWED_HOSTS)
print(type(EMAIL_HOST), EMAIL_HOST)
print(type(EMAIL_HOST_USER), EMAIL_HOST_USER)
print(type(EMAIL_HOST_PASSWORD), EMAIL_HOST_PASSWORD)
print(type(EMAIL_PORT), EMAIL_PORT)
print(type(EMAIL_USE_TLS ), EMAIL_USE_TLS )
print(type(EMAIL_USE_SSL), EMAIL_USE_SSL)
print(type(SERVER_EMAIL), SERVER_EMAIL)
