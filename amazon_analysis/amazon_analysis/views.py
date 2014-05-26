from django.shortcuts import render

def home(request):

    return render(request, 'amazon_analysis/home.html')