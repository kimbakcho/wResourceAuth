from django.urls import path

from authTest.views import authTest

urlpatterns = [
    path('test/', authTest.as_view(), name="test"),
]
