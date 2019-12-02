from django.urls import path

from .views import SignUpView

urlpatterns = [
	path('signup/', SignUpView.as_view(), name='signup'),  # name means how it appears as browser's url
]