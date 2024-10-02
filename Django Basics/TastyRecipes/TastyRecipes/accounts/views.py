from django.http import HttpResponse
from django.shortcuts import render, redirect

from TastyRecipes.accounts.forms import CreateProfileForm, DeleteProfileForm, EditProfileForm
from TastyRecipes.accounts.models import Profile


# Create your views here.

def profile_details(request):
    profile = Profile.get_last_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'details-profile.html', context)

def create_profile(request):

    form = CreateProfileForm(request.POST or None)

    if form and form.is_valid():
        form.save()
        return redirect(to='catalogue')

    context = {
        'form' : form,
    }

    return render(request, 'create-profile.html', context)

def delete_profile(request):

    profile = Profile.get_last_profile()
    form = DeleteProfileForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            profile.delete()
            return redirect(to='home')

    context = {
        'form': form,
    }

    return render(request, 'delete-profile.html', context)

def edit_profile(request):
    profile = Profile.get_last_profile()
    form = EditProfileForm(request.POST or None, instance=profile)

    if form and form.is_valid():
        form.save()
        return redirect(to='home')

    context = {
        'form': form,
    }

    return render(request, 'edit-profile.html', context)
