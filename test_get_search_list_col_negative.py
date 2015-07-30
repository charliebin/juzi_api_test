#coding:utf-8
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json

def test_get_search_list_col_without_uid_and_keyword():
	#list three default data
	#pdb.set_trace()
	response = get_search_list_col('','')
	j_res=json.loads(response.text)
	assert j_res['code'] == 10003
	assert j_res['msg'] != ""
	assert j_res['err'] != ""

def test_get_search_list_col_without_keyword_but_with_uid():
	#list three default data
	#pdb.set_trace()
	response = get_search_list_col(10049,'')
	j_res=json.loads(response.text)
	assert j_res['code'] == 10003
	assert j_res['msg'] != ""
	assert j_res['err'] != ""
def test_get_search_list_col_without_uid_but_with_keyword():
	#list three default data
	#pdb.set_trace()
	response = get_search_list_col('','范冰冰')
	j_res=json.loads(response.text)
	assert j_res['code'] == 10003
	assert j_res['msg'] != ""
	assert j_res['err'] != ""
def test_get_search_list_col_with_unusal_keyword():
	#pdb.set_trace()
	response = get_search_list_col(10049,'  范   冰   冰   ')
	j_res=json.loads(response.text)
	assert j_res['code'] == 20000
	assert j_res['msg'] != ""
	assert j_res['err'] != ""
def test_get_search_list_col_with_keyword_and_unusal_uid():
	#pdb.set_trace()
	response = get_search_list_col('xyz','范冰冰')
	j_res=json.loads(response.text)
	assert  j_res['code'] == 10003
	assert j_res['err'] != ""
def test_get_search_list_col_with_keyword_and_large_uid():
	#pdb.set_trace()
	response = get_search_list_col(100000000,'范冰冰')
	j_res=json.loads(response.text)
	assert j_res['code'] == 20000
	assert j_res['err'] != ""
def test_get_search_list_col_with_keyword_and_minus_uid():
	#pdb.set_trace()
	response = get_search_list_col(-1,'范冰冰')
	j_res=json.loads(response.text)
	assert j_res['code'] == 10003
	assert j_res['err'] != ""
def test_get_search_list_col_with_largepge_minus_size():
	#pdb.set_trace()
	response = get_search_list_col(10049,'范冰冰',10000,1)
	j_res=json.loads(response.text)
	if j_res['code'] == 1:
		assert j_res['data']['page'] ==10000
		assert j_res['data'] != ""
	else:
		assert j_res['code']==20000
def test_get_search_list_col_with_minus_size():
	#pdb.set_trace()
	response = get_search_list_col(10049,'范冰冰',2,2)
	j_res=json.loads(response.text)
	if j_res['code'] == 1:  
		assert j_res['data']['page'] ==2
		assert j_res['data'] != ""
	else:
		assert j_res['code']==20000
                                    
