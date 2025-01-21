from django.shortcuts import redirect,render, get_object_or_404
from django.http import Http404
from django.contrib import messages
from .models import Task, Category, Comment
from .forms import TaskForm, CategoryForm, CommentForm

def index_view(request):
    """
    View untuk menampilkan daftar semua task.
    """
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'uas/index.html', context)

def detail_view(request, task_id):
    """
    View untuk menampilkan detail dari sebuah task.
    Raises Http404 jika task tidak ditemukan.
    """
    try:
        task = Task.objects.get(pk=task_id)
        context = {
            'task': task
        }
    except Task.DoesNotExist:
        raise Http404("Task tidak ditemukan.")
    return render(request, 'uas/detail.html', context)

def create_view(request):
    """
    View untuk membuat task baru.
    Menggunakan TaskForm untuk validasi input.
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = TaskForm(request.POST)
            new_task.save()
            messages.success(request, 'Sukses Menambah Task baru.')
            return redirect('uas:index')
    else:
        form = TaskForm()
    return render(request, 'uas/form.html', {'form': form})

def update_view(request, task_id):
    """
    View untuk mengubah task yang sudah ada.
    Raises Http404 jika task tidak ditemukan.
    """
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task tidak ditemukan.")

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sukses Mengubah Task.')
            return redirect('uas:index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'uas/form.html', {'form': form})

def delete_view(request, task_id):
    """
    View untuk menghapus task.
    Raises Http404 jika task tidak ditemukan.
    """
    try:
        task = Task.objects.get(pk=task_id)
        task.delete()
        messages.success(request, 'Sukses Menghapus Task.')
        return redirect('uas:index')
    except Task.DoesNotExist:
        raise Http404("Task tidak ditemukan.")

# Category Views
def category_list(request):
    """
    View untuk menampilkan daftar kategori.
    """
    categories = Category.objects.all()
    return render(request, 'uas/category/index.html', {'categories': categories})

def category_detail(request, category_id):
    """
    View untuk menampilkan detail kategori dan task-task di dalamnya.
    """
    category = get_object_or_404(Category, pk=category_id)
    tasks = category.tasks.all()
    return render(request, 'uas/category/detail.html', {
        'category': category,
        'tasks': tasks
    })

def category_create(request):
    """
    View untuk membuat kategori baru.
    """
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kategori berhasil dibuat.')
            return redirect('uas:category_list')
    else:
        form = CategoryForm()
    return render(request, 'uas/category/form.html', {'form': form})

def category_update(request, category_id):
    """
    View untuk mengubah kategori yang sudah ada.
    """
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kategori berhasil diperbarui.')
            return redirect('uas:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'uas/category/form.html', {'form': form})

def category_delete(request, category_id):
    """
    View untuk menghapus kategori.
    """
    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    messages.success(request, 'Kategori berhasil dihapus.')
    return redirect('uas:category_list')

# Comment Views
def comment_create(request, task_id):
    """
    View untuk menambahkan komentar pada task.
    """
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.save()
            messages.success(request, 'Komentar berhasil ditambahkan.')
            return redirect('uas:detail', task_id=task_id)
    else:
        form = CommentForm()
    return render(request, 'uas/comment/form.html', {
        'form': form,
        'task': task
    })

def comment_update(request, comment_id):
    """
    View untuk mengubah komentar.
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Komentar berhasil diperbarui.')
            return redirect('uas:detail', task_id=comment.task.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'uas/comment/form.html', {
        'form': form,
        'task': comment.task
    })

def comment_delete(request, comment_id):
    """
    View untuk menghapus komentar.
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    task_id = comment.task.id
    comment.delete()
    messages.success(request, 'Komentar berhasil dihapus.')
    return redirect('uas:detail', task_id=task_id)