from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Splash and Auth
    path('', views.splash, name='splash'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Tasks
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    
    # Subtasks
    path('tasks/<int:task_pk>/subtasks/create/', views.subtask_create, name='subtask_create'),
    path('subtasks/<int:pk>/edit/', views.subtask_edit, name='subtask_edit'),
    path('subtasks/<int:pk>/delete/', views.subtask_delete, name='subtask_delete'),
]

