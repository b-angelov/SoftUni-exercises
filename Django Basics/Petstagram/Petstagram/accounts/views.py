from django.shortcuts import render

# Create your views here.

def register(request):
    context = {

    }

    return render(request, 'accounts/register-page.html', context)

def login(request):
    context = {

    }

    return render(request, 'accounts/login-page.html', context)

def profile_details(request, pk):
    context = {

    }

    return render(request, 'accounts/profile-details-page.html', context)

def profile_edit(request, pk):
    context = {

    }

    return render(request, 'accounts/profile-edit-page.html', context)

def profile_delete(request, pk):
    context = {

    }

    return render(request, 'accounts/profile-delete-page.html', context)
