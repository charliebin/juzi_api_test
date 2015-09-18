#coding:utf-8
import sys
sys.path.append("..")
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json
def test_get_search_list_without_keyword_and_uid():
	#pdb.set_trace()
	response = get_search_list()
	j_res=json.loads(response.text)
	assert j_res['code'] == 10003
	assert j_res['msg'] != ""
	assert j_res['err'] != ""
def test_get_search_list_without_keyword():
	#list three default data
	#pdb.set_trace()
	response = get_search_list()
	j_res=json.loads(response.text)
	assert j_res['code'] == 10003
	assert j_res['err'] != ""
def test_get_search_list_with_empty_keyword():
	#list three default data
	#pdb.set_trace()
	response = get_search_list()
	j_res=json.loads(response.text)
	assert j_res['code'] == 10003
	assert j_res['err'] != ""
def test_get_search_list_with_unusal_keyword():
	#pdb.set_trace()
	response = get_search_list('','  范   冰   冰   ')
	j_res=json.loads(response.text)
	assert response.status_code == 200
	assert j_res['code'] == 20000
	assert j_res['msg'] != ""
	assert j_res['err'] != ""
def test_get_search_list_keyword_with_blank():
	#pdb.set_trace()
	response = get_search_list('','    范冰冰     ')
	j_res=json.loads(response.text)
	assert response.status_code == 200
	assert j_res['code'] == 1
	assert j_res['data'] != ""
	assert j_res['data']['words']!=""
def test_get_search_list_with_keyword_and_unusal_uid():
	#pdb.set_trace()
	response = get_search_list('xyz','范冰冰')
	j_res=json.loads(response.text)
	assert response.status_code == 200
	if j_res['code'] == 1:
		assert j_res['data'] != ""
		assert len(j_res['data']['list']) !=0
		assert len(j_res['data']['col'])==0
		assert j_res['data']['words']!=""
def test_get_search_list_with_keyword_and_large_uid():
	#pdb.set_trace()
	response = get_search_list(100000000,'范冰冰')
	j_res=json.loads(response.text)
	assert response.status_code == 200
	if j_res['code'] == 1:
		assert j_res['data'] != ""
		assert len(j_res['data']['list']) !=0
		assert len(j_res['data']['col'])==0
		assert j_res['data']['words']!=""
def test_get_search_list_with_keyword_and_minus_uid():
	#pdb.set_trace()
	response = get_search_list(-1,'范冰冰')
	j_res=json.loads(response.text)
	assert response.status_code == 200
	if j_res['code'] == 1:
		assert j_res['data'] != ""
		assert len(j_res['data']['list']) !=0
		assert len(j_res['data']['col'])==0
		assert j_res['data']['words']!=""
