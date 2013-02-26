from django.db import models
from django.db.models import signals
from uuid import uuid4

# Create your models here.
class Key(models.Model):
    api_key = models.CharField(max_length=100, default='')

    def __init__(self, *args, **kwargs):
        super(Key, self).__init__(*args, **kwargs)
        if self.api_key == '':
            self.api_key = uuid4().hex
