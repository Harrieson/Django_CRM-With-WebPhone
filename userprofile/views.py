from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .models import Userprofile


def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Userprofile.objects.create(user=user)
            return redirect('/log-in/')
    else: 
        form = UserCreationForm()

    return render(request, 'userprofile/signup.html', {
        'form': form
    })