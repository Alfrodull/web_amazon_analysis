from django.shortcuts import render
import simplejson as json
import urllib
from category import datahelper

# Create your views here.
def index(request):
	target_url = 'http://112.124.1.3:8004/api/commodity/'
	category_list = json.loads(urllib.urlopen(target_url).read())
	context = {'category_list': category_list}
	return render(request, 'category/index.html', context)

def chart(request, cate_name):
	cate_data = datahelper.get_category(cate_name,3)
	star_info_li = datahelper.get_cate_star(cate_data)
	star_num = [0,0,0,0,0]
	for item in star_info_li:
		star_num[0] += item['5']
		star_num[1] += item['4']
		star_num[2] += item['3']
		star_num[3] += item['2']
		star_num[4] += item['1']
	sum = star_num[0] + star_num[1] + star_num[2] + star_num[3] + star_num[4]

	infoli = datahelper.get_revNo_avgstar(cate_data)
	asin_list = []
	rev_count_list = []
	avgstar_list = []
	for item in infoli:
		asin_list.append(item['ASIN'].encode())
		rev_count_list.append(item['review_count'])
		avgstar_list.append(float(item['avg_star']))

	context = {'cate_name': cate_name, \
			   'star_num': star_num, \
			   'asin_list': asin_list, \
			   'rev_count_list': rev_count_list,\
			   'avgstar_list': avgstar_list
			  }
	return render(request, 'category/chart.html', context)

