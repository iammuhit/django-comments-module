from django.urls import path

from . import views

app_name = 'app.modules.comments'

urlpatterns = [
    path('', views.index, name='comments.index'),
]
