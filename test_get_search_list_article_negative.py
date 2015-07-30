#coding:utf-8
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json

def test_get_search_list_article_without_keyword():
	#list three default data
	#pdb.set_trace()
	response = get_search_list_article('','')
	j_res=json.loads(response.text)
	assert j_res['code'] == 10003
	assert j_res['msg'] != ""
	assert j_res['err'] != ""
def test_get_search_list_article_with_empty_keyword():
	#list three default data
	#pdb.set_trace()
	response = get_search_list_article('','')
	j_res=json.loads(response.text)
	assert j_res['code'] == 10003
	assert j_res['msg'] != ""
	assert j_res['err'] != ""
def test_get_search_list_article_with_unusal_keyword():
	#pdb.set_trace()
	response = get_search_list_article('','  范   冰   冰   ')
	j_res=json.loads(response.text)
	assert j_res['code'] == 20000
	assert j_res['msg'] != ""
	assert j_res['err'] != ""
def test_get_search_list_article_with_keyword_and_unusal_uid():
	#pdb.set_trace()
	response = get_search_list_article('xyz','范冰冰')
	j_res=json.loads(response.text)
	assert response.status_code == 200
	if j_res['code'] == 1:
		assert j_res['data'] != ""
		assert len(j_res['data']['list']) !=0
def test_get_search_list_article_with_keyword_and_large_uid():
	#pdb.set_trace()
	response = get_search_list_article(100000000,'范冰冰')
	j_res=json.loads(response.text)
	assert response.status_code == 200
	if j_res['code'] == 1:
		assert j_res['data'] != ""
		assert len(j_res['data']['list']) !=0
def test_get_search_list_article_with_keyword_and_minus_uid():
	#pdb.set_trace()
	response = get_search_list_article(-1,'范冰冰')
	j_res=json.loads(response.text)
	assert response.status_code == 200
	if j_res['code'] == 1:
		assert j_res['data'] != ""
		assert len(j_res['data']['list']) !=0
def test_get_search_list_article_with_largepage_minus_size():
	#pdb.set_trace()
	response = get_search_list_article(10049,'范冰冰',10000,1)
	j_res=json.loads(response.text)
	if j_res['code'] == 1:  
		assert j_res['data']['page'] ==10000
		assert j_res['data'] != ""
	else:
		assert j_res['code']==20000

def test_get_search_list_article_with_minus_size():
	#pdb.set_trace()
	response = get_search_list_article(10049,'范冰冰',2,2)
	j_res=json.loads(response.text)
	if j_res['code'] == 1:  
		assert j_res['data']['page'] ==2
		assert j_res['data'] != ""
	else:
		assert j_res['code']==20000
