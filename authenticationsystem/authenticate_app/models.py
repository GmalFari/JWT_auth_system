from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save
import uuid
from django.contrib.auth.models import( AbstractUser,
                                        BaseUserManager,
                                        PermissionsMixin,
                                        AbstractBaseUser,
                                        Group
                                        )
from django.utils.translation import gettext as _
from django.db import models
from .utils import (path_file_name,
                    generate_slugify_for_instance
                    )

class UserAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,email,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        email = email.lower()
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,first_name,last_name, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser,PermissionsMixin):
    # Usertype choices
    USER_TYPE_CHOICES = (
        ('normal', 'Normal'),
        ('admin', 'Admin'),
        ('staff', 'Staff'),
    )

    groups = models.ManyToManyField(
        Group,
        related_name='user_accounts',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_accounts',
        blank=True
    )
    slug = models.SlugField(unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True,max_length=255)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='normal')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        created = not self.pk  # Check if the object is being created
        super().save(*args, **kwargs)
        if created:
            # Assign the user to him user_type
            if self.user_type == 'normal':
                group = Group.objects.get(name='usersGroup')
            elif self.user_type == 'admin':
                group = Group.objects.get(name='adminsGroup')
            elif self.user_type == 'staff':
                group = Group.objects.get(name='usersGroup')
            else:
                group = None

            if group:
                self.groups.add(group)
    class Meta:
        verbose_name = "user account"
        verbose_name_plural = "Users accounts"
    
''' this siginals will use when the user create new account to generate slug
    this will help us to generate slug field with unique 
    For example 
    first user was irst_name Jamal , last_name farea will get "jamalfarea" slug
    second user was first_name Jamal , last_name farea will get "jamalfarea-322823" slug

'''

def user_account_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    if instance.slug is None:
        fields_values = [instance.first_name,instance.last_name]
        generate_slugify_for_instance(instance,fields_values, save=False)

pre_save.connect(user_account_pre_save, sender=UserAccount)


# this siginals will use when the user create new account to generate slug

def user_account_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    if created:
        fields_values = [instance.first_name,instance.last_name]
        generate_slugify_for_instance(instance,fields_values, save=True)

post_save.connect(user_account_post_save, sender=UserAccount)

class UserProfile(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)
    name= models.CharField(max_length=255,blank=True,null=True)
    coverPhoto = models.ImageField(upload_to=path_file_name,null=True,blank=True)

    # rating = models.IntegerField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # id = models.UUIDField(unique=True,default=uuid.uuid4,editable=False)
    def __str__(self):
        return self.user.first_name
    # class Meta:
    #     abstract = True

    class Meta:
        verbose_name = "user Profile"
        verbose_name_plural = "User Profiles"

        