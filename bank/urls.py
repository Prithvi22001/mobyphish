from django.urls import path
from . import views

urlpatterns = [
    path('bank_login/', views.bank_login, name='bank_login'),
    path('withdraw/', views.withdraw, name='withdraw'),

    # path("withdraw/<str:to>/<int:price>/", views.withdraw, name='withdraw'),

    # path('transactions/<str:user_id>/', views.user_transactions, name='user_transactions'),
]
