from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from .forms import UserCreationForm, UserLoginForm
from web_project import TemplateLayout
from web_project.template_helpers.theme import TemplateHelper
import logging

logger = logging.getLogger(__name__)
User = get_user_model()

class AuthView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context.update(
            {
                "layout_path": TemplateHelper.set_layout("layout_blank.html", context),
            }
        )
        return context

class LoginView(AuthView):
    template_name = "auth_login_basic.html"

    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to the dashboard
            else:
                form.add_error(None, "Invalid username or password")
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

class RegistrationView(AuthView):
    template_name = "auth_register_basic.html"

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('auth-login-basic')  # Redirect to the dashboard
        else:
            logger.error("Form errors: %s", form.errors)
            context = self.get_context_data(form=form)
            return self.render_to_response(context)
