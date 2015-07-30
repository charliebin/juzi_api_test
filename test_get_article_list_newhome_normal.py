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
		
