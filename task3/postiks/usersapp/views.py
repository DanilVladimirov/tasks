from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from usersapp.forms import RegUserForm
from django.utils.decorators import method_decorator
from django.views import View


class RegUserView(View):
    template_name = 'usersapp/register-page.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        context = {}
        form = RegUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Аккаунт создан :)')
            return redirect('login-page')
        else:
            print(form.errors)
            context.update({'form': form})
        return render(request, self.template_name, context)


class LoginUserView(View):
    template_name = 'usersapp/login-page.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('start-page')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        context = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Успешный вход')
            return redirect('start-page')
        else:
            messages.error(request, 'Неверные данные для входа')
        return render(request, self.template_name)


def logout_user(request):
    logout(request)
    messages.success(request, 'Успешный выход')
    return redirect('login-page')
