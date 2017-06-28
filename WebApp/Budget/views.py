from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Expense



def index(request):
    all_budget = Expense.objects.all()
    return render(request, 'budget/index.html', {'all_budget': all_budget})


def detail(request, budget_id):
    expense = get_object_or_404(Expense, pk=budget_id)
    return render(request, 'budget/detail.html', {'expense': expense})

def months(request, month_id):
    month_id = month_id.lower()
    diction = {'january':'01','february':'02','march':'03','april':'04','may':'05','june':'06','july':'07','august':'08','september':'09','october':'10','november':'11','december':'12'}
    try:
        diction[month_id]
        convert = diction[month_id]
        inputs_month = Expense.objects.filter(date__month=convert)
        return render(request, 'budget/months.html', {'inputs_month': inputs_month})
    except KeyError:
        raise Http404(month_id + ' is not a month!')

def generic(request):
    return render(request, 'budget/generic.html')

def elements(request):
    return render(request, 'budget/elements.html')

def all_months(request):
    months = ['January','February','March', 'April', 'May','June','July','August','September','October','November','December'];
    return render(request, 'budget/all_months.html', {'months' : months})