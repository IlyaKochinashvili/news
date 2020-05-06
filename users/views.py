from django.shortcuts import redirect, render

from news.tasks import send_emails
from users.forms import UserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            created_user = form.save()
            my_group = Group.objects.get(name='users')
            my_group.user_set.add(created_user)
            send_emails(form.cleaned_data.get('email'))
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'registration/signup.html', {'form': form})
