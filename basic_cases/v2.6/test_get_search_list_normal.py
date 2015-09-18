#coding:utf-8
import sys
sys.path.append("..")
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json

def test_get_search_list_with_keyword():
	#pdb.set_trace()
	response = get_search_list('','范冰冰')
	j_res=json.loads(response.text)
	assert response.status_code == 200
	if j_res['code'] == 1:
		assert j_res['data'] != ""
		assert len(j_res['data']['list']) !=0
		assert len(j_res['data']['col']) ==0
		assert len(j_res['data']['words'])!=0

def test_get_search_list_with_uid_and_keyword():
	#pdb.set_trace()
	response = get_search_list(10049,'范冰冰')
	j_res=json.loads(response.text)
	assert response.status_code == 200
	if j_res['code'] == 1:
		assert j_res['data'] != ""
		assert len(j_res['data']['list']) !=0
		assert len(j_res['data']['col']) == 1
		assert len(j_res['data']['words']) !=0
