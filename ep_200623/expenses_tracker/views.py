from django.shortcuts import render, redirect

from ep_200623.expenses_tracker.forms import AddExpenseForm, \
    DeleteExpenseForm, DeleteProfileForm, AddProfileForm
from ep_200623.expenses_tracker.models import Profile, Expense


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index_with_profile(request):
    template = 'home-with-profile.html'

    # redirect if no profile
    a_profile = get_profile()
    if a_profile is None:
        return redirect('index no profile')
    # -----------------------

    all_objects = Expense.objects.all()
    money_left = a_profile.budget - sum([x.price for x in all_objects])

    context = {
        'all_objects': all_objects,
        'profile': a_profile,
        'money_left': money_left,
    }
    return render(request, template, context)


def index_no_profile(request):
    template = 'home-no-profile.html'

    # just on case ----------
    if get_profile() is not None:
        return redirect('index with profile')
    # -----------------------

    if request.method == 'POST':
        form = AddProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index with profile')
    else:
        form = AddProfileForm()

    context = {
        'form': form,
    }
    return render(request, template, context)


def create_expense(request):
    template = 'expense-create.html'

    if request.method == 'POST':
        form = AddExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index with profile')
    else:
        form = AddExpenseForm()

    context = {
        'form': form,
    }
    return render(request, template, context)


def edit_expense(request, pk):
    template = 'expense-edit.html'
    current_object = Expense.objects.get(pk=pk)

    if request.method == 'POST':
        form = AddExpenseForm(request.POST, instance=current_object)
        if form.is_valid():
            form.save()
            return redirect('index with profile')
    else:
        form = AddExpenseForm(instance=current_object)

    context = {
        'form': form,
        'current_object': current_object,
    }
    return render(request, template, context)


def delete_expense(request, pk):
    template = 'expense-delete.html'
    current_object = Expense.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, instance=current_object)
        if form.is_valid():
            form.save()
            return redirect('index with profile')
    else:
        form = DeleteExpenseForm(instance=current_object)

    context = {
        'form': form,
        'current_object': current_object,
    }
    return render(request, template, context)


def profile(request):
    template = 'profile.html'
    a_profile = get_profile()

    all_objects = Expense.objects.all()
    money_left = a_profile.budget - sum([x.price for x in all_objects])
    items_bought = len(all_objects)

    context = {
        'current_object': a_profile,
        'money_left': money_left,
        'items_bought': items_bought,
    }
    return render(request, template, context)


def edit_profile(request):
    template = 'profile-edit.html'
    a_profile = get_profile()

    if request.method == 'POST':
        form = AddProfileForm(request.POST, request.FILES, instance=a_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AddProfileForm(instance=a_profile)

    context = {
        'form': form,
        'current_object': a_profile,
    }
    return render(request, template, context)


def delete_profile(request):
    template = 'profile-delete.html'
    a_profile = get_profile()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=a_profile)
        if form.is_valid():
            form.save()
            return redirect('index no profile')
    else:
        form = DeleteProfileForm(instance=a_profile)

    context = {
        'form': form,
        'current_object': a_profile,
    }
    return render(request, template, context)
