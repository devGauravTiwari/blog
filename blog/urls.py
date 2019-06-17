from django.urls import path
from .views import *

urlpatterns=[
	path('',PostListView.as_view(),name='posts'),
	path('post/<int:pk>/',PostDetailView.as_view(),name='post'),
]