from django.shortcuts import render


def index_with_profile(request):
    template = 'home-with-profile.html'

    context = {
    }
    return render(request, template, context)


def index_no_profile(request):
    template = 'home-no-profile.html'

    context = {
    }
    return render(request, template, context)


def create_expense(request):
    template = 'expense-create.html'

    context = {
    }
    return render(request, template, context)


def edit_expense(request, pk):
    template = 'expense-edit.html'

    context = {
    }
    return render(request, template, context)


def delete_expense(request, pk):
    template = 'expense-delete.html'

    context = {
    }
    return render(request, template, context)


def profile(request):
    template = 'profile.html'

    context = {
    }
    return render(request, template, context)


def edit_profile(request):
    template = 'profile-edit.html'

    context = {
    }
    return render(request, template, context)


def delete_profile(request):
    template = 'profile-delete.html'

    context = {
    }
    return render(request, template, context)
