from django.urls import path

from .views import CreateView

app_name = 'questions'

urlpatterns = [
    # path('', ListView.as_view(), name='list'),
     path('create', CreateView.as_view(), name='create'),
    # path('<slug:slug>', DetailView.as_view(), name='detail'),
    # path('update/<slug:slug>', UpdateView.as_view(), name='update')
]
