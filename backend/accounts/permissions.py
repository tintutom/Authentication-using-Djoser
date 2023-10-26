from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

User = get_user_model()

# Create a custom permission for Users
user_content_type = ContentType.objects.get_for_model(User)
user_permission, _ = Permission.objects.get_or_create(
    codename='is_user',
    name='Is User',
    content_type=user_content_type,
)

# Create a custom permission for Doctors
doctor_permission, _ = Permission.objects.get_or_create(
    codename='is_doctor',
    name='Is Doctor',
    content_type=user_content_type,
)
