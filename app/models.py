from django.db import models
import re
class UserManager(models.Manager):
    def basic_validater(self,postData):
        errors={}
        if len(postData['fname'])<2:
            errors['fname']="First name should be at least 2 charcter"
        fname_regex=re.compile(r'^[a-zA-Z]')
        if not fname_regex.match (postData['fname']): 
            errors['fname']="First name should be charcter only"
        if not fname_regex.match (postData['lname']): 
            errors['lname']="Last name should be charcter only"
        if len(postData['lname'])<2:
            errors['lname']="Last name should be at least 2 charcter"
        EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']="INvalid Email !"
        if len(postData['pass'])<8:
            errors['pass']="password should be at least 8 charchter"
        if postData['pass']!=postData['confirm']:
            errors['confirm']="password dont match!"
        return errors
    
class User(models.Model):
    first=models.CharField(max_length=225)
    last=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    password=models.CharField(max_length=225)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

# Create your models here.
