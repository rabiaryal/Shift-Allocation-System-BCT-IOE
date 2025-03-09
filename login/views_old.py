from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from .models import HRManager
from .serializers import HRManagerSerializer

class HRManagerAPI(APIView):
    def get(self, request):
        # Fetch all HRManagers
        query_set = HRManager.objects.all()
        serializer = HRManagerSerializer(query_set, many=True)
        return Response({
            'data': serializer.data,
            'status': True
        })

    def post(self, request):
        """
        Authenticate the HR Manager using ManagerID and password.
        """
        manager_id = request.data.get("ManagerID")
        password = request.data.get("password")

        try:
            manager = HRManager.objects.get(ManagerID=manager_id)

            # Debugging: Print the hashed password and the entered password
            print("Stored Hashed Password:", manager.password)
            print("Entered Password:", password)
            
            # Check if the provided password matches the stored hash
            if check_password(password, manager.password):
                return Response({
                    "message": "Login successful",
                    "status": True
                }, status=200)
            else:
                return Response({
                    "message": "Invalid Manager ID or Password",
                    "status": False
                }, status=401)  # 401 Unauthorized

        except HRManager.DoesNotExist:
            return Response({
                "message": "Manager ID not found",
                "status": False
            }, status=404)  # 404 Not Found, more specific error
