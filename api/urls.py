from django.urls import path
from . import views
from .views import signup, login

urlpatterns = [
    path('todos/', views.TodoListCreate.as_view()),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete', views.TodoToggleComplete.as_view()),
    # path('signup/', views.signup)
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
]
