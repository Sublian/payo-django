from django.contrib import admin
from django.urls import path, include
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
# from users.views import TokenObtainPairView

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("api/", include("users.urls")),
    # path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("api/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("api/", include("products.urls")),
]
