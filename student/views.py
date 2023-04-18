from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Student
from .permissions import UserPermission
from .studentserializer import StudentSerializer

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [permissions.IsAuthenticated,UserPermission]
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        email = data.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error":"user does not exist"})
        data['userid']= user.id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
