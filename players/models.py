from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models


class PlayerManager(BaseUserManager):
    
    #WHen you add fields to this model, you must also add them to the Serializers file!
    
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )

        account.set_password(password)
        account.balance = 100
        account.save()

        return account
    
    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.balance = 100000
        account.save()

        return account



class PlayerAccount(AbstractBaseUser):
    email = models.EmailField( unique=True)
    username = models.CharField(max_length=50, unique=True)
    
    balance = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    #hands_played = models.IntegerField()
    #best_hand = models.CharField(max_length=10)
    
    objects = PlayerManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __unicode__(self):
        return self.email
    
    

# # Create your models here.

# class Player(models.Model):
#     name = models.CharField(max_length=30)
#     games_played = models.IntegerField()
#     games_won = models.IntegerField()
        #hands_played, balance, total credit?
#     current_stack = models.IntegerField()


    

