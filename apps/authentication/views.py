# apps/authentication/views.py

from django.shortcuts import redirect
from django.views.generic import TemplateView
from web_project import TemplateLayout
from web_project.template_helpers.theme import TemplateHelper
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model

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

    def post(self, request, *args, **kwargs):
        if 'auth/register' in request.path:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(**form.cleaned_data)
                login(request, user)
                return redirect('auth-login-basic')  # Redirect to the home page or success page
            else:
                context = self.get_context_data(form=form)
                return self.render_to_response(context)
        elif 'auth/login' in request.path:
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('auth-login-basic')  # Redirect to the home page or success page
            context = self.get_context_data(form=form)
            return self.render_to_response(context)
        else:
            return self.render_to_response(self.get_context_data())

    # def get(self, request, *args, **kwargs):
    #     if 'auth/register' in request.path:
    #         form = UserCreationForm()
    #         context = self.get_context_data(form=form)
    #         return self.render_to_response(context)
    #     elif 'auth/login' in request.path:
    #         form = AuthenticationForm()
    #         context = self.get_context_data(form=form)
    #         return self.render_to_response(context)
    #     return super().get(request, *args, **kwargs)
