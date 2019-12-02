from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')  # if signup was successfully, reverse user to login page
	template_name = 'signup.html'  # html used to display the page