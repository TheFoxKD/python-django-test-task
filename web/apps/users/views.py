from typing import override

from django.contrib.auth import get_user_model, login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from .forms import CustomUserCreationForm

User = get_user_model()


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('core:shop:list')

    @override
    def form_valid(self, form: CustomUserCreationForm):
        self.object: User = form.save()
        login(self.request, self.object)
        return HttpResponseRedirect(self.get_success_url())


class LoginView(FormView):
    pass
