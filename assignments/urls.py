from django.urls import path
from . import views


urlpatterns = [
    path('safeEndpoint/', views.SafeEndpoint.as_view())

]
