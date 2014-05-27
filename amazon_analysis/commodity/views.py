from django.shortcuts import render, render_to_response

from commodity import datahelper

def index(request):
	return render(request, 'commodity/index.html')

def search(request):
	asin = request.GET['asin']
	product_data = datahelper.get_product_data(asin)
	if product_data:
		com_name = product_data['productInfo'][0]['name']

		zlink = 'http://www.amazon.com/dp/'+asin

		#
		star_list = datahelper.get_star_list(product_data)
		star_sum = [0,0,0,0,0]
		for star in star_list:
			if star == 5: star_sum[0]+=1
			elif star == 4: star_sum[1]+=1
			elif star == 3: star_sum[2]+=1
			elif star == 2: star_sum[3]+=1
			elif star == 1: star_sum[4]+=1
			else: pass
		#
		price_date_li = datahelper.get_price_list(product_data)
		price_list = []
		date_list = []
		for price_date in price_date_li:
			price_list.append(price_date[0]);
			date_list.append(str(price_date[1].split()[0]))
		#
		review_time = datahelper.get_review_time_list(product_data)
		count_list = review_time[0]
		date_li2 = review_time[1]
		context = {
			'asin': asin, \
			'com_name': com_name, \
			'zlink': zlink, \
			'star_sum': star_sum, \
			'price_list': price_list, \
			'date_list': date_list, \
			'count_list': count_list, \
			'date_li2': date_li2
		}

	else:
		context = {'asin': ''}
	return render_to_response('commodity/chart.html', context)
