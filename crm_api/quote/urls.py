from django.urls import path
from quote import views

app_name = 'quote'
urlpatterns = [
    path('quotes/', views.QuoteList.as_view(), name='quote_list'),
    path('quotes/<int:pk>/', views.QuoteDetail.as_view(), name='quote_detail'),
]