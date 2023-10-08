from django.urls import path
from accounts.views import account, login, register, resert_password

urlpatterns = [
    path('account/', account, name='account'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('resert_password/', resert_password, name='resert_password'),
]
