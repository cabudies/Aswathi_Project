from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.AccountantLoginView.as_view(),name='login'),
    path('approve_payment/',views.approve_payment,name='approve-payment'),
    path('cash_payement/',views.cash_payments,name='cash-payments'),
    path('payment_details/',views.get_payment_details,name='cash-payments'),

]