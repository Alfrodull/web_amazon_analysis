from django.shortcuts import render, render_to_response

def index(request):
	return render(request, 'commodity/index.html')

def search(request):
	asin = request.GET['asin']
	context = {'asin': asin}
	return render_to_response('commodity/chart.html', context)
