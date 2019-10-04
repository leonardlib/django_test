from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view()),
    path('', RedirectView.as_view(url='players/')),
    path('', include('players.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
