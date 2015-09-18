import sys
sys.path.append("..")
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json

def test_get_article_list_newhome_with_large_size_and_page():

	'''
	even with large page and size parameter, api should handler correctly.

	'''
	response = get_article_list_home(uid=10049,page=999, size=999)
	assert response.status_code == 200
	j_res = json.loads(response.text)
	assert j_res['code'] == 20000
	assert j_res['msg'] != ""
	assert j_res['err'] != ""

def test_get_article_list_newhome_with_minus_size_and_page():
	response = get_article_list_home(page=-1, size=-1)
	j_res = json.loads(response.text)
	#print response.text
	assert j_res['code'] == 1
	assert j_res['msg'] != ""
	assert j_res['data'] != ""
	assert j_res['data']['page'] !=-1

def test_get_article_list_newhome_with_minus_size_and_large_page():
	response = get_article_list_home(uid=10049,page=99999999, size=1)
	j_res = json.loads(response.text)
	#print response.text
	if(j_res['code'] == 1):
		assert j_res['data']['page'] ==100
		assert j_res['data'] != ""
	else:
		assert j_res['code'] == 20000
		assert j_res['err'] != ""
	assert j_res['msg'] != ""

def test_get_article_list_newhome_with_unusal_size_and_page():
	response = get_article_list_home(page='xy', size='xy')
	j_res = json.loads(response.text)
	#print response.text
	assert j_res['code'] == 1
	assert j_res['msg'] != ""
	assert j_res['data'] != ""
	assert j_res['data']['page'] != 'xy'
def test_get_article_list_newhome_with_unusal_uid():
	response = get_article_list_home(uid="abcd")
	j_res = json.loads(response.text)
	#print response.text
	assert j_res['code'] == 1
	assert j_res['msg'] != ""
	assert j_res['data'] != ""

