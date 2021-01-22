import requests
import re
from lxml import etree
from bs4 import BeautifulSoup
from flask import jsonify, request
import json
import sys

session = requests.session()

def findcourse(dept, sub):

	print("GET Course....")
	testquerys = {
		'year': '109',  # 學年
		'sms': '2',  # 學期
		'dgr_id': '14',  # 14=日間部
		'unt_id': '%',  # 科系
		'ls_clslong': '%',  # 遠距課程
		'cls_id': '%',  # 通識課程
		'clyear': '',  # 年級
		'sub_name': sub,  # 科目
		'teacher': '',  # 教師
		'week': '%',  # 星期
		'period': '%',  # 節次
		'pgm_id': '%',  # 學程課程
		'yms_year': '109',
		'yms_sms': '2',
		'reading': 'reading',
	}
	print("tes2")
	requ = session.post("https://as2.npu.edu.tw/npu/ag_pro/ag202.jsp", data=testquerys, timeout=10)
	print("tes3")
	soup = BeautifulSoup(requ.text, 'html.parser')
	a_tags = soup.find_all('td')
	i = 20

	coutable=[]
	for test in a_tags:
		try:
			cselect = int(a_tags[i + 12].string.strip())-int(a_tags[i + 11].string.strip())
		except:
			continue
		if cselect < 0 :
			cselect = 0
		courseinfo = {
			'cou_dorn': a_tags[i].string.strip(),
			'cou_dept': a_tags[i+1].string.strip(),
			'cou_class': a_tags[i+2].string.strip(),
			'cou_id': a_tags[i + 3].string.strip(),
			'cou_name': a_tags[i + 4].string.strip(),
			'cou_score':a_tags[i + 5].string.strip(),
			'cou_times':a_tags[i + 6].string.strip(),
			'cou_requ': a_tags[i + 7].string.strip(),
			'cou_teach': a_tags[i+9].string.strip(),
			'cou_room': a_tags[i + 10].string.strip(),
			'cou_nowp':  a_tags[i + 11].string.strip(),
			'cou_maxp':  a_tags[i + 12].string.strip(),
			'cou_date': a_tags[i + 13].string.strip(),
			'cou_info': a_tags[i + 14].string.strip(),
			'canselect': cselect
		}
		coutable.append(courseinfo)
		i += 15
		print(courseinfo)
		if i >= len(a_tags):
			break
	return json.dumps(coutable)


