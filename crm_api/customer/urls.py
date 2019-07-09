from django.urls import path
from customer import views

app_name = 'customer'
urlpatterns = [
    path('customers/', views.CustomerList.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerDetail.as_view(), name='customer-detail'),
]