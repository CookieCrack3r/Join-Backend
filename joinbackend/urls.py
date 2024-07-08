
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from join import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'task_category', views.TaskCategoryViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'boards', views.BoardViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login/', views.LoginView.as_view(), name='api_login_auth'),
    path('api/signup/', views.UserCreateView.as_view(), name='user_create'),
    path('api/current_user/', views.CurrentUserView.as_view(), name='user_create'),
    path('api/guest_exists/', views.GuestUserExistsView.as_view(), name='guest_exists'),
    path('api/check_token/', views.CheckTokenView.as_view(), name='check_token')
]
