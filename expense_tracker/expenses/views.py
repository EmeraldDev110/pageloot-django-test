from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import User, Expense
from .serializers import UserSerializer, ExpenseSerializer
from datetime import datetime

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    @action(detail=False, methods=['get'])
    def list_by_date_range(self, request):
        user_id = request.query_params.get('user_id')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not user_id or not start_date or not end_date:
            return Response({"error": "user_id, start_date, and end_date are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            expenses = Expense.objects.filter(
                user_id=user_id,
                date__range=[start_date, end_date]
            )
            serializer = self.get_serializer(expenses, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def category_summary(self, request):
        user_id = request.query_params.get('user_id')
        month = request.query_params.get('month')

        if not user_id or not month:
            return Response({"error": "user_id and month are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            expenses = Expense.objects.filter(
                user_id=user_id,
                date__month=datetime.strptime(month, '%Y-%m').month
            ).values('category').annotate(total=Sum('amount'))
            return Response(expenses)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
