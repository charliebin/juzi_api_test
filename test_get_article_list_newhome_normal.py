from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json

def test_get_article_list_newhome_default():
	#pdb.set_trace()
	response = get_article_list_newhome()
	j_res=json.loads(response.text)
	assert response.status_code == 200
	assert j_res['code'] == 1
	assert j_res['msg'] != ""
	assert j_res['data'] != ""
	assert j_res['data']['page'] == 1
	childList = j_res['data']['list']
	index=0
	for item in childList:
		if index>=0 and index<=2:
			assert item.has_key('type')==false
		elif index==3:
			assert item.has_key('type')==true
			assert  item['type']==3
		elif index >=4 and index <=7:
			assert item.has_key('type')==false
		elif index==8:
			assert item.has_key('type')==true
			assert  item['type']==1
		elif index >=9 and index <=13:
			assert item.has_key('type')==false
		elif index==14:
			if  item.has_key('type')==true:
				assert  item['type']==2
			else:
				assert item.has_key('type')==false
		index+=1
		if index>=15:
			index-=15


def test_get_article_list_newhome_with_uid():
	#pdb.set_trace()
	response = get_article_list_newhome(10000)
	j_res = json.loads(response.text)
	assert response.status_code == 200
	assert j_res['code'] == 1
	assert j_res['msg'] != ""
	assert j_res['data'] != ""
	assert j_res['data']['page'] == 1

def test_get_article_list_newhome_with_page():
	#pdb.set_trace()
	response = get_article_list_newhome(uid=10049,page=10)
	j_res = json.loads(response.text)
	assert response.status_code == 200
	assert j_res['code'] == 1
	assert j_res['msg'] != ""
	assert j_res['data'] != ""
	assert j_res['data']['page'] == 10
		
