#coding:utf-8
import sys
sys.path.append("..")
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json
import  time
def test_get_comment_list_user_without_uid():
	#pdb.set_trace()
	response = get_comment_list_user(uid='',page='',size='',sort='')
	j_res = json.loads(response.text)
	assert j_res['code'] == 10003
	assert j_res['msg'] != ""
	assert j_res['err'] != ""

def test_get_comment_list_user_with_unusal_uid():
	#pdb.set_trace()
	response = get_comment_list_user(uid='xyz',page='',size='',sort='')
	j_res = json.loads(response.text)
	assert j_res['code'] == 10003
	assert j_res['msg'] != ""
	assert j_res['err'] != ""

def test_get_comment_list_user_with_large_size_and_page():
	#pdb.set_trace()
	response = get_comment_list_user(uid=473451,page=999,size=999,sort='')
	j_res = json.loads(response.text)
	assert response.status_code == 200
	assert j_res['code'] == 20000
	assert j_res['msg'] != ""
	assert j_res['err'] != ""
def test_get_comment_list_user_with_unusal_size_and_page():
	response =get_comment_list_user(uid=473451,page=-1, size=-1,sort='')
	j_res = json.loads(response.text)
	#print response.text
	assert j_res['code'] == 1
	assert j_res['msg'] != ""
	assert j_res['data'] != ""
	assert j_res['data']['page'] !=-1

def test_get_comment_list_user_with_page_and_minus_size():
	#pdb.set_trace()
	response = get_comment_list_user(uid=473451,page=10,size=1,sort='')
	j_res = json.loads(response.text)
	assert response.status_code == 200
	if  j_res['code']==1:
			assert j_res['msg'] != ""
			assert j_res['data'] != ""
			assert j_res['data']['page'] == 10
	else:
			assert j_res['code'] == 20000
			assert j_res['msg'] != ""
			assert j_res['err'] != ""
def  test_get_comment_list_user_with_minus_size_and_large_page():
	response = get_comment_list_user(uid=473451,page=99999999, size=1,sort='')
	j_res = json.loads(response.text)
	#print response.text
	if(j_res['code'] == 1):
		assert j_res['data']['page'] ==100
		assert j_res['data'] != ""
	else:
		assert j_res['code'] == 20000
		assert j_res['err'] != ""
	assert j_res['msg'] != ""
def test_get_comment_list_user_with_unusal_size_and_page():
	response = get_comment_list_user(uid=473451,page='xy', size='xy',sort='')
	j_res = json.loads(response.text)
	#print response.text
	assert j_res['code'] == 1
	assert j_res['msg'] != ""
	assert j_res['data'] != ""
	assert j_res['data']['page'] != 'xy'
def test_get_comment_list_user_with_unusal_sort():
	#pdb.set_trace()
	response = get_comment_list_user( uid=473451,page='',size='',sort='defg')
	j_res = json.loads(response.text)
	assert response.status_code == 200
	if  j_res['code'] == 1:
		assert j_res['data']['page'] == 1
		assert j_res['msg'] != ""
		assert j_res['data'] != ""
		for i in range(len(j_res['data']['list'])):
			assert j_res['data']['list'][i]['user']['id']==473451
			if (i+1)< len(j_res['data']['list']):
				a_struct_time=time.strptime(j_res['data']['list'][i]['publish_time'],'%Y-%m-%d %H:%M:%S')
				b_struct_time=time.strptime(j_res['data']['list'][i+1]['publish_time'],'%Y-%m-%d %H:%M:%S')
				assert time.mktime(a_struct_time)>time.mktime(b_struct_time)
	else:
		j_res['code'] == 20000
		assert j_res['msg'] != ""
		assert j_res['err'] != ""
	
def test_get_comment_list_user_with_unusal_sort_and_page():
	#pdb.set_trace()
	response = get_comment_list_user( uid=473451,page=2,size=3,sort='defg')
	j_res = json.loads(response.text)
	assert response.status_code == 200
	if  j_res['code'] == 1:
		assert j_res['data']['page'] == 2
		assert len(j_res['data']['list']) == 3
		assert j_res['msg'] != ""
		assert j_res['data'] != ""
		for i in range(len(j_res['data']['list'])):
			assert j_res['data']['list'][i]['user']['id']==473451
			if (i+1)< len(j_res['data']['list']):
				a_struct_time=time.strptime(j_res['data']['list'][i]['publish_time'],'%Y-%m-%d %H:%M:%S')
				b_struct_time=time.strptime(j_res['data']['list'][i+1]['publish_time'],'%Y-%m-%d %H:%M:%S')
				assert time.mktime(a_struct_time)>time.mktime(b_struct_time)
	else:
		j_res['code'] == 20000
		assert j_res['msg'] != ""
		assert j_res['err'] != ""
	
