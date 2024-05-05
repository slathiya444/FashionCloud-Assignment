from django.utils import timezone
import uuid


class CreatedAtMixin:
    def __init__(self):
        self.created_at = timezone.now()

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class UUIDGenerator:
    @staticmethod
    def generate_uuid():
        return str(uuid.uuid4())
