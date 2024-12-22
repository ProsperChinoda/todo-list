from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('index', views.index, name='index'),
    path('edit/<int:id>', views.edit_todo, name='edit'),
    path('delete_todo/<int:id>', views.delete_todo),
]

