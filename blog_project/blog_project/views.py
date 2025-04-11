from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView


class BaseView(View):
    template_name = "base.html"

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)

class RegisterView(CreateView):
    template_name = "register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")