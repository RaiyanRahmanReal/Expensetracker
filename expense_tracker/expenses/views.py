from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Expense, Category
from .forms import ExpenseForm, ExpenseFilterForm
from django.db.models import Sum

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_expenses')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    expense.delete()
    return redirect('view_expenses')

def modify_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('view_expenses')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/modify_expense.html', {'form': form})

def view_expenses(request):
    form = ExpenseFilterForm(request.GET)
    expenses = Expense.objects.all()
    if form.is_valid():
        if form.cleaned_data['category']:
            expenses = expenses.filter(category=form.cleaned_data['category'])
        if form.cleaned_data['start_date']:
            expenses = expenses.filter(date__gte=form.cleaned_data['start_date'])
        if form.cleaned_data['end_date']:
            expenses = expenses.filter(date__lte=form.cleaned_data['end_date'])
    return render(request, 'expenses/view_expenses.html', {'expenses': expenses, 'form': form})

def summarize_expenses(request):
    summary = Expense.objects.values('category__name').annotate(total=Sum('amount'))
    return render(request, 'expenses/summarize_expenses.html', {'summary': summary})
def home(request):
    return redirect('view_expenses')
