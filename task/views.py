from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from task.forms import SignUpForm
from task.models import CustomUser


class BaseView(View):
    template_name = 'base_form.html'
    form_class = ''
    title = ''

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())

    def get_context_data(self, **kwargs):
        return {'title': self.title, 'form': self.form_class}

    def post(self, request):
        return render(request, self.template_name, self.get_context_data())


class SignUp(BaseView):
    template_name = 'signup.html'
    form_class = SignUpForm
    title = 'Sign up'

    def get(self, request):
        return super(SignUp, self).get(request)

    def get_context_data(self, **kwargs):
        return {'title': self.title, 'form': self.form_class}

    def post(self, request):
        form = self.form_class(request.POST)
        ctx = self.get_context_data()
        if not form.is_valid():
            ctx["form"] = form
            return render(request, self.template_name, ctx)
        if CustomUser.filter_user(email=form.cleaned_data.get('email')).exists():
            messages.error(request, "User Already Exist")
            return render(request, self.template_name, ctx)
        form.save(commit=False)
        return HttpResponseRedirect(reverse("list_view"))


class IndexView(BaseView):
    template_name = 'index.html'
    title = 'Index Page'

    def get(self, request):
        return render(request, self.template_name, {'title': self.title})


class ListView(View):
    template_name = 'list_page.html'
    title = 'List Page'

    def get(self, request):
        users = CustomUser.filter_user(is_superuser=False)
        return render(request, self.template_name, self.get_context_data(**{'users': users}))

    def get_context_data(self, **kwargs):
        return {'title': self.title,
                'users': kwargs.get('users')}


