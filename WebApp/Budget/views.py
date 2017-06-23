from django.http import Http404
from django.shortcuts import render
from .models import Expense



def index(request):
    all_budget = Expense.objects.all()
    return render(request, 'budget/index.html', {'all_budget': all_budget})


def detail(request, budget_id):
    try:
        expense = Expense.objects.get(pk=budget_id)
    except Expense.DoesNotExist:
        raise Http404('Budget does not exist!')
    return render(request, 'budget/detail.html', {'expense': expense})

def months(request, month_id):
    diction = {'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06','July':'07','August':'08','September':'09','October':'10','November':'11','December':'12'}
    convert = diction[month_id]
    try:
        inputs_month = Expense.objects.filter(date__month=convert)
    except Expense.DoesNotExist:
        raise Http404('Month Does Not Exist!')
    return render(request, 'budget/months.html', {'inputs_month': inputs_month})