from django.urls import path

from .views import schedule_veiw, UsersListView, GenerateRandomUserView

urlpatterns = [
    path('', schedule_veiw, name='home'),
    path('user-list', UsersListView.as_view(), name='users_list'),
    path('generate-user', GenerateRandomUserView.as_view(), name='generate_user'),
]
