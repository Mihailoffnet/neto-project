from django.test import TestCase

# Create your tests here.

import os
from dotenv import load_dotenv
load_dotenv()

print(os.getenv("EMAIL_HOST_USER"))
print(os.getenv("DEBUG"))
print(type(bool(os.getenv("DEBUG"))))