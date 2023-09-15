from rest_framework import generics,permissions
from .models import UserAccount,UserProfile
from .serializers import UserAccountSerializer,UserProfileSerializer


class UserAccountListCreateView(generics.ListCreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer


class UserAccountRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    lookup_field = 'id'



class UserProfileCreateView(generics.CreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer


class UserAccountRetrieveUpdateView(generics.RetrieveDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'