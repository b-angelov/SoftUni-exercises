from django.http import HttpResponse
from django.shortcuts import render, redirect

from TastyRecipes.accounts.models import Profile
from TastyRecipes.common.templatetags.user_profile import user_profile
from TastyRecipes.recipes.forms import CreateRecipeForm, DeleteRecipeForm
from TastyRecipes.recipes.models import Recipe


# Create your views here.

def catalogue_page(request):

    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, 'catalogue.html', context)

def create_recipe(request):

    if not request.user.is_authenticated:
        return HttpResponse('This page is only available for authenticated users')

    form = CreateRecipeForm(request.POST or None)

    if form and form.is_valid():
        profile = Profile.get_last_profile()
        form = form.save(commit=False)
        form.author_id = profile.pk
        form.save()
        return redirect(to='catalogue')

    context = {
        "form" : form,
    }

    return render(request, 'create-recipe.html', context)

def recipe_details(request, recipe_id):

    recipe = Recipe.objects.get(pk=recipe_id)

    context = {
        'recipe': recipe,
        'ingredients': recipe.ingredients.split(', '),
    }

    return render(request, 'details-recipe.html', context)

def recipe_edit(request, recipe_id):

    if not request.user.is_authenticated:
        return HttpResponse('This page is only available for authenticated users')

    recipe = Recipe.objects.get(pk=recipe_id)
    form = CreateRecipeForm(request.POST or None, instance=recipe)

    if form and form.is_valid():
        form.save()
        return redirect(to='catalogue')

    context = {
        "form" : form,
    }

    return render(request, 'edit-recipe.html', context)

def recipe_delete(request, recipe_id):

    if not request.user.is_authenticated:
        return HttpResponse('This page is only available for authenticated users')

    recipe = Recipe.objects.get(pk=recipe_id)

    if request.method == 'POST':
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe.delete()
            return redirect(to='catalogue')
    else:
        form = DeleteRecipeForm(instance=recipe)


    context = {
        "form": form,
    }

    return render(request, 'delete-recipe.html', context)