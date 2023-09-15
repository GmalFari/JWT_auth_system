from django.urls import path
from .views import(
       UserAccountListCreateView,
         UserAccountRetrieveUpdateView,
         UserProfileCreateView,
         UserAccountRetrieveUpdateView
        )
urlpatterns = [
    # user account
    path('accounts/', UserAccountListCreateView.as_view(), name='user-account-list-create'),
    path('accounts/<int:id>/', UserAccountRetrieveUpdateView.as_view(), name='user-account-retrieve-update'),
    # user profile
    path('profile/', UserProfileCreateView.as_view(), name='user-account-list-create'),
    path('profile/<int:id>/', UserAccountRetrieveUpdateView.as_view(), name='user-profile-retrieve-update-delete'),
]