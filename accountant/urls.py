from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.AccountantLoginView.as_view(),name='login'),
    path('all_transactions/',views.all_transactions,name='all_trans'),
    path('approve_payment/',views.approve_payment,name='approve-payment'),
    path('add_cash/',views.add_cash,name='add-cash')

]