from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class AboutView(LoginRequiredMixin, TemplateView):
    template_name = 'about.html'


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'
