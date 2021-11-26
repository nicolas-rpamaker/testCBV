from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_view),
    path('createpoll/', views.CreatePollView.as_view()),
    path('updatepoll/<int:pk>', views.UpdatePollView.as_view())
    , path('list/', views.ListPollsView.as_view())
]
