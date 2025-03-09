from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password

class HRManagerCustom(models.Manager):       
 
    def create_user(self,ManagerID, email, username, password=None):
        if not ManagerID:
            raise ValueError("The ManagerID field must be set")
        if not username:
            raise ValueError("Users must have a username")
        if not email:
            raise ValueError('The Email field must be set')
        email = email.lower()
        user = self.model(ManagerID=ManagerID,  email=email, username=username)
        if password:
            user.password = make_password(password)
        user.save(using=self._db)
        return user
    

class HRManager(models.Model):
    id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=50)
    ManagerID = models.CharField(
        max_length=4,
        validators=[RegexValidator(r'^\d{4}$', 'Manager ID must be exactly 4 digits')],
        unique=True,
        default='0000'
    )
    password = models.CharField(max_length=128)  # Increased max_length to accommodate hashed passwords

    username = models.CharField(max_length=150, default='HRManager')

    email = models.EmailField(unique=True, default= 'hrmanager@gmail.com')

    objects = HRManagerCustom()

    def save(self, *args, **kwargs):
        # If password is not already hashed, hash it before saving
        if not self.password.startswith('pbkdf2_sha256$'):  # Checking if the password is already hashed
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)



