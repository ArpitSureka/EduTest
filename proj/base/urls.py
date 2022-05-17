from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile_update, name='profile_update'),
    path('question/<int:pk>', views.detail_view, name='question-detail'),
    path('answers/<int:pk>', views.answer_form, name='answer-form'),
]
