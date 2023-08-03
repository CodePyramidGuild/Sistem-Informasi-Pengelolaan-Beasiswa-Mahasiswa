from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Beasiswa(models.Model): 
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()

    def __str__(self):
        return self.nama

class Mahasiswa(models.Model): 
    nama = models.CharField(max_length=100)
    nim = models.CharField(max_length=20)
    email = models.EmailField()
    alamat = models.TextField()

    def __str__(self):
        return self.nama

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff
