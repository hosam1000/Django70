# apps/authentication/views.py

from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth import login
from web_project import TemplateLayout
from web_project.template_helpers.theme import TemplateHelper
from .forms import UserRegistrationForm


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
        if 'auth_register_basic' in request.path:
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.save()
                login(request, user)
                return redirect('index')  # Redirect to a success page
            else:
                return self.render_to_response(self.get_context_data(form=form))
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if 'auth_register_basic' in request.path:
            form = UserRegistrationForm()
            return self.render_to_response(self.get_context_data(form=form))
        return super().get(request, *args, **kwargs)
