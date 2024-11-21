from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ExpenseViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('expenses', ExpenseViewSet, basename='expense')

urlpatterns = router.urls
