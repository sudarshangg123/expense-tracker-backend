from django.urls import path
from .views import CreateExpenseView, ListExpenseView, ExpenseAnalyticsView

urlpatterns = [
    path('expenses/', CreateExpenseView.as_view(), name='create-expense'),
    path('expenses/list/', ListExpenseView.as_view(), name='list-expense'),
    path('expenses/analytics/', ExpenseAnalyticsView.as_view(), name='analytics-expense'),
]
