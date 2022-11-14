
from django.urls import path

from ResourceAuth.views import TokenView, VerifiedView, RevokeTokenView, TestView

urlpatterns = [
    path('token/', TokenView.as_view()),
    path('verified/', VerifiedView.as_view()),
    path('revoke/', RevokeTokenView.as_view()),
    path('test/', TestView.as_view())
]
