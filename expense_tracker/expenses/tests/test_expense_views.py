from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Expense
from django.urls import reverse
from datetime import date

class ExpenseAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a user
        self.user = User.objects.create(username="testuser", email="testuser@example.com")

        # Create expenses for the user
        self.expense1 = Expense.objects.create(
            user=self.user,
            title="Lunch",
            amount=20,
            date=date(2024, 11, 1),
            category="Food",
        )
        self.expense2 = Expense.objects.create(
            user=self.user,
            title="Taxi",
            amount=50,
            date=date(2024, 11, 5),
            category="Travel",
        )

        self.expense_url = reverse("expense-list-create")
        
    def test_create_expense(self):
        payload = {
            "user": self.user.id,
            "title": "Groceries",
            "amount": 100,
            "date": "2024-11-10",
            "category": "Food",
        }
        response = self.client.post(self.expense_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Expense.objects.count(), 3)
        self.assertEqual(Expense.objects.last().title, "Groceries")
        
    def test_list_expenses(self):
        response = self.client.get(self.expense_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Two expenses created in `setUp`
    
    def test_retrieve_expense(self):
        url = reverse("expense-detail", kwargs={"pk": self.expense1.id})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Lunch")
        
    def test_update_expense(self):
        url = reverse("expense-detail", kwargs={"pk": self.expense1.id})
        payload = {"title": "Brunch"}
        response = self.client.patch(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.expense1.refresh_from_db()
        self.assertEqual(self.expense1.title, "Brunch")
        
    
    def test_delete_expense(self):
        url = reverse("expense-detail", kwargs={"pk": self.expense1.id})
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Expense.objects.count(), 1)  # Only one expense remains
        
    def test_expenses_by_date_range(self):
        url = reverse("expenses-by-date-range", kwargs={
            "user_id": self.user.id,
            "start_date": "2024-11-01",
            "end_date": "2024-11-03",
        })
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only `expense1` falls in the range
        self.assertEqual(response.data[0]["title"], "Lunch")
        
    def test_category_summary(self):
        url = reverse("category-summary", kwargs={
            "user_id": self.user.id,
            "year": 2024,
            "month": 11,
        })
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Two categories: Food and Travel
        self.assertEqual(response.data[0]["category"], "Food")
        self.assertEqual(response.data[0]["total"], 20)

