from django.db import models
import re 

class UserManager(models.Manager):
    def create_validator(self, reqPOST):
        errors = {}
        email_checker = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(reqPOST['first_name']) <2 or len(reqPOST['last_name']) <2:
            errors['name'] = "Name must be at least 2 characters"
        if not email_checker.match(reqPOST['email']):
            errors['email'] = "Email must be valid"
        if len(reqPOST['password']) < 8:
            errors['password'] = "Password must be at least 8 chcaracters"
        if reqPOST['password'] != reqPOST['confpassword']:
            errors['password'] = "Passwords do not match!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

