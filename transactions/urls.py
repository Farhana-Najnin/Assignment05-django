from django.urls import path
from .views import DepositeFormView
urlpatterns = [
    path('deposite/',DepositeFormView.as_view(), name='deposit'),
]