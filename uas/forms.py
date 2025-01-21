from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Task, Category, Comment

class TaskForm(ModelForm):
    """
    Form untuk membuat dan mengubah Task.
    """
    class Meta:
        model = Task
        fields = ('title', 'description', 'status', 'category')
        labels = {
            'title': _('Judul'),
            'description': _('Deskripsi'),
            'status': _('Status'),
            'category': _('Kategori')
        }
        error_messages = {
            'title': {
                'required': _("Judul harus diisi."),
            },
            'description': {
                'required': _("Deskripsi harus diisi."),
            },
        }

class CategoryForm(ModelForm):
    """
    Form untuk membuat dan mengubah Category.
    """
    class Meta:
        model = Category
        fields = ('name', 'description')
        labels = {
            'name': _('Nama Kategori'),
            'description': _('Deskripsi')
        }
        error_messages = {
            'name': {
                'required': _("Nama kategori harus diisi."),
            },
        }

class CommentForm(ModelForm):
    """
    Form untuk membuat dan mengubah Comment.
    """
    class Meta:
        model = Comment
        fields = ('content',)
        labels = {
            'content': _('Komentar')
        }
        error_messages = {
            'content': {
                'required': _("Komentar harus diisi."),
            },
        }