from django.urls import path
import blog_apps.views

urlpatterns = [
    path('to_do', blog_apps.views.to_do, name='list'),
    path('to_do/update_task/<str:pk>/', blog_apps.views.updateTask, name="update_task"),
    path('to_do/delete/<str:pk>/', blog_apps.views.deleteTask, name="delete")
]
