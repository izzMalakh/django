from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        if len(postData['fname']) < 2:
            errors["first_name"] = "first name name should be at least 2 characters"

        if len(postData['lname']) < 2:
            errors["last_name"] = "last name name should be at least 2 characters"

        if len(postData['password']) < 8:
            errors["password"] = "password should be at least 8 characters"
        if postData['password'] != postData['cpassword']:
            errors["cpassword"] = "passwords does not match!"
        
        if len(postData['email']) == 0:
            errors["email"] = "email is empty!"
        users= User.objects.all()
        for user in users:
            if user.email == postData['email']:
                errors['email']="this email already selected before in our database"
        # another solution : 
        # if User.objects.filter(email__contains=postData['email']):
        #     errors["email"] = "email in our datebase!! try another one!!"
        
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid Email Address!"
        

        return errors
    
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()