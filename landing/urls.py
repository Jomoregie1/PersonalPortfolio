from django.urls import path
from landing import views

app_name = 'landing'

urlpatterns = [
    path('', views.all_projects, name='all_projects'),
    path('<int:pk>', views.project_detail, name='project_detail')
]
