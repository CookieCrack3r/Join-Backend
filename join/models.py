import datetime
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.forms import JSONField


class Board(models.Model):
    
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    created_at = models.DateField(("Date"), default=datetime.date.today)
    users = models.ManyToManyField(User, related_name="boards")

    def __str__(self):
        return self.title
    
    
    
class TaskCategory(models.Model): 
    
    category = models.CharField(max_length=30)
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.category

class Task(models.Model):
   
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('inprogress', 'In Progress'),
        ('awaitfeedback', 'Awaiting Feedback'),
        ('done', 'Done'),
    ]
    PRIO_CHOICES = [
        ('urgent','urgent' ),
        ('medium','medium'),
        ('low',"low"),
    ]

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200, blank=True)
    users = models.ManyToManyField(User, related_name='tasks') 
    due_date = models.DateField(("Date"), default=datetime.date.today)
    priority = models.CharField(max_length=20, choices=PRIO_CHOICES, default='low')
    category = models.ForeignKey(TaskCategory, related_name='tasks', on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name='tasks', on_delete=models.CASCADE)
    subtasks = models.JSONField(default=list, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')

    def __str__(self):
        return self.title