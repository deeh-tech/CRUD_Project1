from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name='home'),
    path('emp', views.createEmp, name='create_emp'),
    path('show', views.show, name='show_emp'),
    path('edit/<int:id>', views.edit, name='edit_emp'),
    path('update/<int:id>', views.update, name='update_emp'),
    path('delete/<int:id>', views.destroy, name='delete_emp'),
]