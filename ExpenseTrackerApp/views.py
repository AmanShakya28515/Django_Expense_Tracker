from rest_framework import viewsets, permissions
from .models import ExpenseIncome
from .serializers import ExpenseAndIncomeSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


class IsOwnerOrSuperuser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.user == request.user
    

class ExpenseIncomeViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseAndIncomeSerializer
    permission_classes = [IsOwnerOrSuperuser]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ExpenseIncome.objects.all()
        return ExpenseIncome.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            from .serializers import ExpenseListSerializer
            return ExpenseListSerializer
        return ExpenseAndIncomeSerializer


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])  
def register_user(request):
    if request.method == 'GET':
        return Response({
            "message": "Send a POST request with 'username' and 'password' to register."
        }, status=200)

    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "Username and password are required."}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=400)

    User.objects.create_user(username=username, password=password)
    return Response({"message": "User registered successfully"}, status=201)

