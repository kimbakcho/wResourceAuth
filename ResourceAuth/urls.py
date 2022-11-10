

from django.contrib import admin
from django.urls import path, include

from ResourceAuth.views import TokenView, VerifiedView

urlpatterns = [
    path('token/', TokenView.as_view()),
    path('Verified/', VerifiedView.as_view())
]
