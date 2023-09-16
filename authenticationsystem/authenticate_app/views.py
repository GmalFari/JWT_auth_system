from rest_framework import generics,permissions
from .models import UserAccount,UserProfile
from .serializers import UserAccountSerializer,UserProfileSerializer



class UserAccountListView(generics.ListAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

class UserAccountRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    lookup_field = 'slug'
    partial = True  # Allow partial updates via PATCH

class UserProfileCreateView(generics.CreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer


class UserProfileRetrieveUpdateView(generics.RetrieveDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'slug'

  