from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    # ex: /polls/5/
    path('books/', views.books, name='books'),
    # ex: /polls/5/results/
    path('members/', views.members, name='members'),
    # ex: /polls/5/vote/
    path('statuses/', views.status, name='statuses'),
    path('addstatus/', views.new_status, name='new_status'),
]