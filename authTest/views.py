# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class authTest(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request: Response):
        return Response({"test": "test"})
