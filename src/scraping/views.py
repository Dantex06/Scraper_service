
from django.shortcuts import render
import datetime

def home(request):
   date = datetime.datetime.now().date()
   name = "Victor"
   _context = {'date': date, 'name': name}
   return render(request=request, template_name='home.html', context=_context)