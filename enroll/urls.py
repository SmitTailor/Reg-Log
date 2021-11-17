from django.urls import path
from . import views
urlpatterns = [
    path('', views.sign_in, name = 'sign_in'),
    path('signup/', views.sign_up, name = 'signup'),
    path('add_show/<int:id>/', views.add_show, name = 'add_show'),
    path('delete/<int:id>/', views.delete_data, name = 'deletedata'),
    path('update/<int:id>/', views.update_data, name = 'updatedata'),
]