from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied, ValidationError
from django.db import IntegrityError
from django.http import Http404, HttpResponseServerError
from django.utils import timezone
from .models import Task, Subtask
from .forms import SignupForm, LoginForm, TaskForm, SubtaskForm


def splash(request):
    """Splash screen with auto-redirect to login."""
    return render(request, 'tasks/splash.html')


def signup(request):
    """User registration with error handling."""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        try:
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}! Please log in.')
                return redirect('login')
            else:
                messages.error(request, 'Please correct the errors below.')
        except ValidationError as e:
            messages.error(request, str(e))
        except IntegrityError:
            messages.error(request, 'An error occurred. Please try again.')
    else:
        form = SignupForm()
    
    return render(request, 'tasks/signup.html', {'form': form})


def user_login(request):
    """User login with error handling."""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please fill in all fields.')
    else:
        form = LoginForm()
    
    return render(request, 'tasks/login.html', {'form': form})


@login_required
def dashboard(request):
    """Dashboard with task summary."""
    try:
        user_tasks = Task.objects.filter(user=request.user)
        total_tasks = user_tasks.count()
        completed_tasks = user_tasks.filter(status='Completed').count()
        in_progress_tasks = user_tasks.filter(status='In-Progress').count()
        todo_tasks = user_tasks.filter(status='To Do').count()
        high_priority = user_tasks.filter(priority='High', status__in=['To Do', 'In-Progress']).count()
        
        recent_tasks = user_tasks[:5]
        
        context = {
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'in_progress_tasks': in_progress_tasks,
            'todo_tasks': todo_tasks,
            'high_priority': high_priority,
            'recent_tasks': recent_tasks,
        }
        return render(request, 'tasks/dashboard.html', context)
    except Exception as e:
        messages.error(request, 'An error occurred while loading the dashboard.')
        return render(request, 'tasks/dashboard.html', {
            'total_tasks': 0,
            'completed_tasks': 0,
            'in_progress_tasks': 0,
            'todo_tasks': 0,
            'high_priority': 0,
            'recent_tasks': [],
        })


@login_required
def task_list(request):
    """List all tasks with search and filter."""
    try:
        tasks = Task.objects.filter(user=request.user)
        
        # Search functionality
        search_query = request.GET.get('search', '')
        if search_query:
            tasks = tasks.filter(title__icontains=search_query) | tasks.filter(description__icontains=search_query)
        
        # Filter by priority
        priority_filter = request.GET.get('priority', '')
        if priority_filter:
            tasks = tasks.filter(priority=priority_filter)
        
        # Filter by status
        status_filter = request.GET.get('status', '')
        if status_filter:
            tasks = tasks.filter(status=status_filter)
        
        tasks = tasks.order_by('-created_at')
        
        context = {
            'tasks': tasks,
            'search_query': search_query,
            'priority_filter': priority_filter,
            'status_filter': status_filter,
        }
        return render(request, 'tasks/task_list.html', context)
    except Exception as e:
        messages.error(request, 'An error occurred while loading tasks.')
        return render(request, 'tasks/task_list.html', {'tasks': []})


@login_required
def task_create(request):
    """Create a new task with error handling."""
    if request.method == 'POST':
        form = TaskForm(request.POST, user=request.user)
        try:
            if form.is_valid():
                task = form.save(commit=False)
                task.user = request.user
                task.save()
                messages.success(request, 'Task created successfully!')
                return redirect('task_detail', pk=task.pk)
            else:
                messages.error(request, 'Please correct the errors below.')
        except ValidationError as e:
            messages.error(request, str(e))
        except IntegrityError:
            messages.error(request, 'A task with this title already exists.')
        except Exception as e:
            messages.error(request, 'An error occurred while creating the task.')
    else:
        form = TaskForm(user=request.user)
    
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Create'})


@login_required
def task_detail(request, pk):
    """View task details with ownership verification."""
    try:
        task = get_object_or_404(Task, pk=pk)
        
        # Verify ownership
        if task.user != request.user:
            raise PermissionDenied("You don't have permission to view this task.")
        
        subtasks = task.subtasks.all()
        
        context = {
            'task': task,
            'subtasks': subtasks,
        }
        return render(request, 'tasks/task_detail.html', context)
    except Http404:
        messages.error(request, 'Task not found.')
        return redirect('task_list')
    except PermissionDenied:
        messages.error(request, "You don't have permission to view this task.")
        return redirect('task_list')
    except Exception as e:
        messages.error(request, 'An error occurred while loading the task.')
        return redirect('task_list')


@login_required
def task_edit(request, pk):
    """Edit a task with ownership verification."""
    try:
        task = get_object_or_404(Task, pk=pk)
        
        # Verify ownership
        if task.user != request.user:
            raise PermissionDenied("You don't have permission to edit this task.")
        
        if request.method == 'POST':
            form = TaskForm(request.POST, instance=task, user=request.user)
            try:
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Task updated successfully!')
                    return redirect('task_detail', pk=task.pk)
                else:
                    messages.error(request, 'Please correct the errors below.')
            except ValidationError as e:
                messages.error(request, str(e))
            except IntegrityError:
                messages.error(request, 'A task with this title already exists.')
            except Exception as e:
                messages.error(request, 'An error occurred while updating the task.')
        else:
            form = TaskForm(instance=task, user=request.user)
        
        return render(request, 'tasks/task_form.html', {'form': form, 'task': task, 'action': 'Edit'})
    except Http404:
        messages.error(request, 'Task not found.')
        return redirect('task_list')
    except PermissionDenied:
        messages.error(request, "You don't have permission to edit this task.")
        return redirect('task_list')
    except Exception as e:
        messages.error(request, 'An error occurred while loading the task.')
        return redirect('task_list')


@login_required
def task_delete(request, pk):
    """Delete a task with ownership verification."""
    try:
        task = get_object_or_404(Task, pk=pk)
        
        # Verify ownership
        if task.user != request.user:
            raise PermissionDenied("You don't have permission to delete this task.")
        
        if request.method == 'POST':
            try:
                task.delete()
                messages.success(request, 'Task deleted successfully!')
                return redirect('task_list')
            except Exception as e:
                messages.error(request, 'An error occurred while deleting the task.')
                return redirect('task_detail', pk=pk)
        
        return render(request, 'tasks/task_confirm_delete.html', {'task': task})
    except Http404:
        messages.error(request, 'Task not found.')
        return redirect('task_list')
    except PermissionDenied:
        messages.error(request, "You don't have permission to delete this task.")
        return redirect('task_list')
    except Exception as e:
        messages.error(request, 'An error occurred.')
        return redirect('task_list')


@login_required
def subtask_create(request, task_pk):
    """Create a subtask with parent task ownership verification."""
    try:
        task = get_object_or_404(Task, pk=task_pk)
        
        # Verify ownership
        if task.user != request.user:
            raise PermissionDenied("You don't have permission to add subtasks to this task.")
        
        if request.method == 'POST':
            form = SubtaskForm(request.POST)
            try:
                if form.is_valid():
                    subtask = form.save(commit=False)
                    subtask.task = task
                    subtask.save()
                    messages.success(request, 'Subtask created successfully!')
                    return redirect('task_detail', pk=task.pk)
                else:
                    messages.error(request, 'Please correct the errors below.')
            except ValidationError as e:
                messages.error(request, str(e))
            except Exception as e:
                messages.error(request, 'An error occurred while creating the subtask.')
        else:
            form = SubtaskForm()
        
        return render(request, 'tasks/subtask_form.html', {'form': form, 'task': task, 'action': 'Create'})
    except Http404:
        messages.error(request, 'Task not found.')
        return redirect('task_list')
    except PermissionDenied:
        messages.error(request, "You don't have permission to add subtasks to this task.")
        return redirect('task_list')
    except Exception as e:
        messages.error(request, 'An error occurred.')
        return redirect('task_list')


@login_required
def subtask_edit(request, pk):
    """Edit a subtask with ownership verification."""
    try:
        subtask = get_object_or_404(Subtask, pk=pk)
        task = subtask.task
        
        # Verify ownership
        if task.user != request.user:
            raise PermissionDenied("You don't have permission to edit this subtask.")
        
        if request.method == 'POST':
            form = SubtaskForm(request.POST, instance=subtask)
            try:
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Subtask updated successfully!')
                    return redirect('task_detail', pk=task.pk)
                else:
                    messages.error(request, 'Please correct the errors below.')
            except ValidationError as e:
                messages.error(request, str(e))
            except Exception as e:
                messages.error(request, 'An error occurred while updating the subtask.')
        else:
            form = SubtaskForm(instance=subtask)
        
        return render(request, 'tasks/subtask_form.html', {'form': form, 'task': task, 'subtask': subtask, 'action': 'Edit'})
    except Http404:
        messages.error(request, 'Subtask not found.')
        return redirect('task_list')
    except PermissionDenied:
        messages.error(request, "You don't have permission to edit this subtask.")
        return redirect('task_list')
    except Exception as e:
        messages.error(request, 'An error occurred.')
        return redirect('task_list')


@login_required
def subtask_delete(request, pk):
    """Delete a subtask with ownership verification."""
    try:
        subtask = get_object_or_404(Subtask, pk=pk)
        task = subtask.task
        
        # Verify ownership
        if task.user != request.user:
            raise PermissionDenied("You don't have permission to delete this subtask.")
        
        if request.method == 'POST':
            try:
                task_pk = task.pk
                subtask.delete()
                messages.success(request, 'Subtask deleted successfully!')
                return redirect('task_detail', pk=task_pk)
            except Exception as e:
                messages.error(request, 'An error occurred while deleting the subtask.')
                return redirect('task_detail', pk=task.pk)
        
        return render(request, 'tasks/subtask_confirm_delete.html', {'subtask': subtask, 'task': task})
    except Http404:
        messages.error(request, 'Subtask not found.')
        return redirect('task_list')
    except PermissionDenied:
        messages.error(request, "You don't have permission to delete this subtask.")
        return redirect('task_list')
    except Exception as e:
        messages.error(request, 'An error occurred.')
        return redirect('task_list')


# Custom error handlers
def custom_404(request, exception):
    """Custom 404 error page."""
    return render(request, 'tasks/404.html', status=404)


def custom_403(request, exception):
    """Custom 403 error page."""
    return render(request, 'tasks/403.html', status=403)


def custom_500(request):
    """Custom 500 error page."""
    return render(request, 'tasks/500.html', status=500)

