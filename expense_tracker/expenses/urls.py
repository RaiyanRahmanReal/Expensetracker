from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_expense, name='add_expense'),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('modify/<int:expense_id>/', views.modify_expense, name='modify_expense'),
    path('view/', views.view_expenses, name='view_expenses'),
    path('summarize/', views.summarize_expenses, name='summarize_expenses'),
]
