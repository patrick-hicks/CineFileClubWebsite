from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, AbstractBaseUser

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import EmailValidator


# class UserManager(BaseUserManager):
#     def create_user(self, email, first_name, last_name, password, company_id = None):
#         if not email:
#             raise ValueError("Users must have an email address.")
#         if not first_name:
#             raise ValueError("Please enter a first name.")
#         if not last_name:
#             raise ValueError("Please enter a last name.")
#         if not password:
#             raise ValueError("Users must have a password.")
        

            
        
#         email = self.normalize_email(email)
#         user = self.model(email = email, first_name = first_name, last_name=last_name, company_id=company_id)
        
#         user.set_password(password)
#         user.save(using = self._db)

#         return user

#     def create_superuser(self, email, first_name, last_name, password, company=None):
#         user = self.create_user(email, first_name, last_name, password, company)
#         user.is_superuser = True
#         user.is_staff = True

#         user.save(using=self._db)

#         return user



class User(AbstractUser):
    pass
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['first_name','last_name']
    
    # id = models.AutoField(primary_key=True)
    
    # is_api_user = models.BooleanField(default=False)
    # username = None
    # email = models.EmailField('email address',unique = True, validators=[EmailValidator])
    # objects = UserManager()

class Movie(models.Model):
    title = models.CharField(null=False, max_length=255)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True)