from django.urls import path

from app.modules.comments import views

app_name = 'app.modules.comments'

urlpatterns = [
    path('', views.index, name='comments.index'),
]
