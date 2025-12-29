from django.urls import path

from app.modules.comments import views

app_name = 'app.modules.comments'

urlpatterns = [
    path('create/', views.create, name='comments.create'),
    path('delete/<int:pk>/', views.delete, name='comments.delete'),
    path('approve/<int:pk>/', views.approve, name='comments.approve'),
]
