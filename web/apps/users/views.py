from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('core:shop:list')


class LoginView(FormView):
    pass
