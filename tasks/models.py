from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    
    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In-Progress', 'In-Progress'),
        ('Completed', 'Completed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To Do')
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = [['user', 'title']]
    
    def clean(self):
        if self.due_date and self.due_date < timezone.now().date():
            raise ValidationError({'due_date': 'Due date cannot be in the past.'})
        
        if self.title:
            self.title = self.title.strip()
            if len(self.title) < 3:
                raise ValidationError({'title': 'Title must be at least 3 characters long.'})
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class Subtask(models.Model):
    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In-Progress', 'In-Progress'),
        ('Completed', 'Completed'),
    ]
    
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To Do')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_at']
    
    def clean(self):
        if self.title:
            self.title = self.title.strip()
            if len(self.title) < 1:
                raise ValidationError({'title': 'Subtask title cannot be empty.'})
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.task.title} - {self.title}"

