from django.utils.translation import gettext_lazy as _
from django.db import models


class Category(models.Model):
    """
    Model Category untuk mengelompokkan task berdasarkan kategori.
    """
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    Model Task untuk menyimpan data tugas/task.
    """
    class TaskStatus(models.TextChoices):
        """
        Enum untuk status task yang tersedia
        """
        TODO = 'todo', _('Todo')
        IN_PROGRESS = 'in_progress', _('In Progress')
        CLOSED = 'closed', _('Closed')
    
    # define columns
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.TODO
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='tasks',
        default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # define table name
        db_table = 'tasks'


class Comment(models.Model):
    """
    Model Comment untuk menyimpan komentar pada task.
    """
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comments'