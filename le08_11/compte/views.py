from django.shortcuts import render, redirect
from django.contrib import messages
from compte.form import Creeruser


def log(request):
    form = Creeruser()
    if request.method == 'POST':
        form = Creeruser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'compte créé' + user)
            return redirect('acces')
    context = {'form': form}
    return render(request,'app/register.html',context)