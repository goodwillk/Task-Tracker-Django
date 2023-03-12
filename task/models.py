from django.db import models
from django.utils import timezone
import datetime

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TaskDetail(BaseModel):
    def assigned():
        return timezone.now() + datetime.timedelta(hours=24)

    task = models.JSONField()           #If not specified, automatically --> blank=False
    estimated_time = models.DateTimeField(default=assigned)
    is_task_completed = models.BooleanField(default=False)
