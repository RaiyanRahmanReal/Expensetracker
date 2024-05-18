from django import forms
from .models import Category, Expense
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'category', 'date', 'description']

class ExpenseFilterForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'category', 'date', 'description']

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero.")
        return amount