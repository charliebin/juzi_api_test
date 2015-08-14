#coding:utf-8
from lib.api_call_functions import *
import pytest
import json
import time

def test_get_common_setting_normal():
	response = get_common_setting()
	j_res = json.loads(response.text)
	#print response.text
	assert j_res['code'] == 1
	assert j_res['msg'] != ""
	assert j_res['data'] != ""
	#文章
	if j_res['data']['splash_m']==0 :
		assert j_res['data']['splash_h']==6166
	#频道，27是频道id，57是频道八卦下的栏目，名字也是八卦，但是含义是不一样的
	elif j_res['data']['splash_m']==1 :
		if j_res['data']['splash_h']==27:
			assert j_res['data']['splash_n']=='八卦'
		elif j_res['data']['splash_h']==57:
			assert j_res['data']['splash_n']=='八卦'
	#tag name is '刘亦菲' tag id is 327
	elif j_res['data']['splash_m']==2:
		assert j_res['data']['splash_h']==327
		assert j_res['data']['splash_n']=='刘亦菲'
	#页面，the page name is needed.
	elif j_res['data']['splash_m']==3:
		assert j_res['data']['splash_h']=='https://www.baidu.com/'
		assert j_res['data']['splash_n']=='百度一下'


