from typing import override

from django.contrib.auth import get_user_model, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, RedirectView

from .forms import CustomAuthenticationForm, CustomUserCreationForm

User = get_user_model()


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('core:shop:list')

    @override
    def get_success_url(self) -> str:
        return self.success_url

    @override
    def form_valid(self, form: CustomUserCreationForm) -> HttpResponseRedirect:
        user: User = form.save()
        login(request=self.request, user=user)
        return HttpResponseRedirect(self.get_success_url())


class LoginView(FormView):
    form_class = CustomAuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('core:shop:list')

    @override
    def get_success_url(self) -> str:
        return self.success_url

    @override
    def form_valid(self, form: CustomAuthenticationForm) -> HttpResponseRedirect:
        user: User = form.get_user()
        login(request=self.request, user=user)
        return HttpResponseRedirect(self.get_success_url())


class LogoutView(RedirectView):
    url = reverse_lazy('core:shop:list')

    @override
    def get_redirect_url(self, *args, **kwargs) -> str:
        logout(request=self.request)
        return super().get_redirect_url(*args, **kwargs)
