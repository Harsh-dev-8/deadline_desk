from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import RegisterSerializer
from rest_framework import status

# Register view
class RegisterAPIView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Your account has been created successfully"}, status=status.HTTP_201_CREATED)

