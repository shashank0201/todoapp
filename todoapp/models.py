from django.db import models

# Create your models here.


STATUS_CHOICES = (
    ("Inprogress", 'Inprogress'),
    ("Completed", 'Completed'),
    ("Pending", 'Pending'),
)   

class Todo(models.Model):
    title = models.CharField(max_length=200)
    Descriptions = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completion_date  = models.DateTimeField(blank=True)
    status = models.CharField(choices=STATUS_CHOICES,  max_length=10)
    visible_status = models.BooleanField(default=True) 

