from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.home, name="home"),

    # CRUD operations
    path('create-task', views.createTask, name='create-task'),
    path('view-form', views.viewTasks, name="viewTasks"),
    path('update-task/<str:pk>/', views.updateTask, name="updateTasks"),
    path('delete-task/<str:pk>/', views.deleteTask, name="deleteTasks"),

    # Dashboard
    path('dashboard', views.dashboard, name="dashboard"),

    # Register a user
    path('register', views.register, name="register"),

    # Login Page
    path('login', views.login, name="login"),

    # Logout Page
    path('logout', views.logout, name="logout"),

]
