from django.contrib.auth.models import User
from django.db import models

class Education(models.Model):
    # Визначте поля для моделі Education
    pass

class Skills(models.Model):
    # Визначте поля для моделі Skills
    pass

class Connections(models.Model):
    # Визначте поля для моделі Connections
    pass

class Messages(models.Model):
    # Визначте поля для моделі Messages
    pass

class Posts(models.Model):
    # Визначте поля для моделі Posts
    pass
class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
from django.db import models
from django.contrib.auth.models import User

class Connection(models.Model):
    STATUS_CHOICES = [
        ('requested', 'Requested'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    sender = models.ForeignKey(User, related_name='sent_connections', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_connections', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='requested')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['sender', 'receiver']
