#-*- coding:utf-8-*-
import urllib
import simplejson as json

def get_category(category,pages):
	'''返回category分类下，从第一页到第pages页的数据，每页20条'''
	baseurl = 'http://112.124.1.3:8004/api/commodity/?category_name='
	condition = '&page='
	data = []

	for i in range(1,int(pages)+1):
		fullpath = baseurl+urllib.quote(category)+condition+str(i)
		datapiece = json.loads(urllib.urlopen(fullpath).read())
		for item in datapiece:
			data.append(item)
	return data

def get_cate_star(cate_data):
	star_info_li = []
	for data in cate_data:
		star_info_li.append(data['stats_info']['star_info'])
	return star_info_li

def get_revNo_avgstar(cate_data):
	infolist = []
	for data in cate_data:
		item = {}
		item['ASIN'] = data['ASIN']
		item['review_count'] = data['stats_info']['review_count']
		item['avg_star'] = data['stats_info']['avg_info']
		infolist.append(item)
	return infolist