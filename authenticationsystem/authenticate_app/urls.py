from django.urls import path
from .views import(
       UserAccountListView,
       UserCreateView,
         UserAccountRetrieveUpdateView,
         UserProfileCreateView,
         UserAccountRetrieveUpdateView
        )
urlpatterns = [
    # user account
    path('register/', UserCreateView.as_view(), name='user-account-list-create'),
    path('accounts/', UserAccountListView.as_view(), name='user-account-list-create'),
    path('accounts/<str:slug>/', UserAccountRetrieveUpdateView.as_view(), name='user-account-retrieve-update'),
    # user profile
    path('profile/', UserProfileCreateView.as_view(), name='user-account-list-create'),
    path('profile/<str:slug>/', UserAccountRetrieveUpdateView.as_view(), name='user-profile-retrieve-update-delete'),
]

