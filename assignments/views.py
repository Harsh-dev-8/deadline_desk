from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

#protected endpoint for test
class SafeEndpoint(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        res = {"message": "Hello world from SafeEndpoint"}
        return Response(res)
