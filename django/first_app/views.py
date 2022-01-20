import re
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    home_text = request.POST['count']
    home_text_count = len(home_text)
    return render(request, 'result.html', {'counts':home_text_count})