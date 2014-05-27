#-*- coding:utf-8-*-
import urllib
import simplejson as json
from datetime import datetime


def get_product_data(asin):
	'''use asin to get get_product_data '''
	target_url = 'http://112.124.1.3:8004/api/commodity/' + asin
	return json.loads(urllib.urlopen(target_url).read())

def get_star_list(product_data):
	'''get star infomation from product data'''
	return [float(single_review['star'].split()[0]) for single_review in product_data['review']]

def get_price_list(product_data):
	'''get first price infomation from product data'''
	price_date_li = []
	for offer in product_data['offer']:
		if offer['info']:
			price_date_li.append((offer['info'][0]['price'],offer['info'][0]['timestamp']))
	return price_date_li

def get_review_time_list(product_data):
	'''get revie and time infomation from product data'''
	time_list = []

	for review in product_data['review']:
		time_list.append(datetime.strptime(review['publishTime'], '%Y-%m-%d %H:%M:%S'))
	time_list = list(set(time_list))    
	review_count_dict = {}

	for single_date in time_list[::-1]:
		review_count_dict[int(single_date.strftime('%Y%m'))] = review_count_dict[int(single_date.strftime('%Y%m'))] + 1 \
			if review_count_dict.has_key(int(single_date.strftime('%Y%m'))) else 1

	review_count_list = sorted(review_count_dict.iteritems(), key=lambda x:x[0])

	count_data = incre_list(map(lambda x:x[1], review_count_list))
	date_data = map(lambda x:datetime.strptime(str(x[0]), '%Y%m'), review_count_list)

	date_str = []
	for t in date_data:
		date_str.append(t.strftime('%Y-%m'))
	return (count_data,date_str)

def incre_list(origin_list):
	'''数组元素递加'''
	return [sum(origin_list[0: idx]) for idx,ele in enumerate(origin_list)]