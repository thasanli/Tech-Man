from django.db import models
import re

# Create your models here.

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$")
# email has been set as type='email'. To make sure do one changed throught inspect

class UserManager(models.Manager):
    def user_validation(self, postData):
        errors = {}
        if len(postData['firstName']) < 2:
            errors['firstName'] = 'First Name should be at least 2 characters'
        if len(postData['lastName']) < 2:
            errors['lastName'] = 'Last Name should be at least 2 characters'
        if len(postData['password']) < 8:
            errors['password'] = 'Password should be at least 8 characters'
        if postData['password'] != postData['confirmPassword']:
            errors['confirmPassword'] = 'Passwords doest match'
        if User.objects.filter(email=postData['email']):
            errors['email'] = 'This email already registered'
        if not EMAIL_REGEX.match(postData['email']):
            errors['invalid_email'] = 'Invalid email adress'
        return errors

class JobSeeker(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Employer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()






