# if add more, need to makemigrate then migrate

from django.db import models

class Expense(models.Model):
    category = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    amount = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
# this makes it show as a value instead of a object    
    def __str__(self):
        return self.description + ': ' + str(self.date)
    
class Input(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    files_type =models.CharField(max_length=20)
    input_title = models.CharField(max_length=200)
    is_favorite = models.BooleanField(default = False)
    def __str__(self):
        return self.expense + ' : ' + self.input_title + self.files_type