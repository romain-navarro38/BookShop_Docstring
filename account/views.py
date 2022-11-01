from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, FormView

from account.forms import UserRegistrationForm, UserEditForm
from account.models import CustomUser


class UserCreateView(CreateView):
    model = CustomUser
    template_name = 'account/signup.html'
    form_class = UserRegistrationForm

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Créer un compte'
        context['submit_text'] = "S'inscrire"
        return context

    def get_success_url(self):
        return reverse('home')


class UserProfileView(FormView):
    model = CustomUser
    template_name = 'account/profile.html'
    form_class = UserEditForm

    def form_valid(self, form):
        user = self.request.user
        user.username = self.request.POST.get('username')
        user.first_name = self.request.POST.get('first_name')
        user.last_name = self.request.POST.get('last_name')
        user.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editer un compte'
        context['submit_text'] = 'Enregistrer les modifications'
        context['form'] = UserEditForm(initial=model_to_dict(self.request.user))
        return context

    def get_success_url(self):
        return reverse('home')


class CustomLoginView(LoginView):
    model = CustomUser
    template_name = 'account/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Se connecter'
        context['submit_text'] = 'Connexion'
        return context

    def get_success_url(self):
        return reverse('home')


class CustomLogoutView(LogoutView):
    def get_success_url(self):
        return reverse("home")


class CustomPasswordChangeView(PasswordChangeView):
    model = CustomUser
    template_name = 'account/password-change.html'

    def get_success_url(self):
        return reverse('account:profile')
