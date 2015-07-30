#coding:utf-8
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json
def test_get_search_list_article_with_keyword():
	#pdb.set_trace()
	response = get_search_list_article('','范冰冰')
	j_res=json.loads(response.text)
	assert response.status_code == 200
	if j_res['code'] == 1:
		assert j_res['data'] != ""
		assert len(j_res['data']['list']) !=0

def test_get_search_list_article_with_uid_and_keyword():
	#pdb.set_trace()
	response = get_search_list_article(10049,'范冰冰')
	j_res=json.loads(response.text)
	if j_res['code'] == 1:
		assert j_res['data'] != ""
		assert len(j_res['data']['list']) !=0
