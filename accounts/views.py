import django.core.handlers.wsgi
from django.shortcuts import render, redirect
from .forms import MsbRegisterForm
from django.contrib.auth.decorators import login_required


def register(request: django.core.handlers.wsgi.WSGIRequest):
    if request.method == 'POST':
        form = MsbRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request=request,
                   template_name='accounts/register.html',
                   context={
                       'form': form
                   })

    elif request.user.is_authenticated:
        return redirect('home')
    else:
        form = MsbRegisterForm()
        return render(request=request,
                      template_name='accounts/register.html',
                      context={
                          'form': form
                      })


@login_required(login_url='/accounts/login')
def home(request):
    return render(request, 'accounts/home.html')
