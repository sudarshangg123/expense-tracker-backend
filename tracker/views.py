from rest_framework import generics, permissions
from rest_framework.response import Response
from django.db.models import Sum, Avg
from django.db.models.functions import TruncDay, TruncWeek, TruncMonth
from .models import Expense
from .serializers import ExpenseSerializer


# ✅ Create a new expense
class CreateExpenseView(generics.CreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ✅ List expenses filtered by date range
class ListExpenseView(generics.ListAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        start = self.request.GET.get('start_date')
        end = self.request.GET.get('end_date')
        queryset = Expense.objects.filter(user=user)
        if start and end:
            queryset = queryset.filter(date__range=[start, end])
        return queryset


# ✅ Full analytics: total, category-wise, daily/weekly/monthly trends
class ExpenseAnalyticsView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user

        # Optional filters
        start = request.GET.get('start_date')
        end = request.GET.get('end_date')

        expenses = Expense.objects.filter(user=user)

        if start and end:
            expenses = expenses.filter(date__range=[start, end])

        # Total Expenses
        total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0

        # Category-wise breakdown
        by_category = expenses.values('category').annotate(total=Sum('amount'))

        # Daily trend
        daily = expenses.annotate(day=TruncDay('date')).values('day').annotate(
            total=Sum('amount'),
            average=Avg('amount')
        )

        # Weekly trend
        weekly = expenses.annotate(week=TruncWeek('date')).values('week').annotate(
            total=Sum('amount'),
            average=Avg('amount')
        )

        # Monthly trend
        monthly = expenses.annotate(month=TruncMonth('date')).values('month').annotate(
            total=Sum('amount'),
            average=Avg('amount')
        )

        return Response({
            "total_expenses": total,
            "category_breakdown": by_category,
            "daily_trend": daily,
            "weekly_trend": weekly,
            "monthly_trend": monthly
        })


