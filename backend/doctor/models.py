# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager,Group,Permission

# class DoctorAccountManager(BaseUserManager):
#     def create_doctor(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('Doctors must have an email address')

#         email = self.normalize_email(email)
#         doctor = self.model(email=email, **extra_fields)

#         doctor.set_password(password)
#         doctor.save()

#         return doctor

# class DoctorAccount(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=True)
#     groups = models.ManyToManyField(Group, related_name='doctor_accounts')
#     user_permissions = models.ManyToManyField(Permission, related_name='doctor_accounts')

#     objects = DoctorAccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']

#     def get_full_name(self):
#         return self.first_name

#     def get_short_name(self):
#         return self.first_name

#     def __str__(self):
#         return self.email
