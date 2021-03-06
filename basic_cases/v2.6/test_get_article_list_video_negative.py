import sys
sys.path.append("..")
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json
import time

def test_get_article_list_video_with_large_page_and_size():
	
	'''large page and large size'''
	response = get_article_list_video(uid=473451,page=999, size=999)
	j_res = json.loads(response.text)
	assert j_res['code'] == 20000
	assert j_res['msg'] != ""
	assert j_res['err'] != ""

def test_get_article_list_video_with_minus_page_and_size():
	
	'''small page and size'''
	response = get_article_list_video( page=-1, size=-1)
	j_res = json.loads(response.text)

	assert j_res['code'] == 1
	assert j_res['msg'] != ""
	assert j_res['data'] != ""
	assert j_res['data']['page'] != -1

def test_get_article_list_video_with_large_page_and_minus_size():
	'''large page and  small size'''
	response = get_article_list_video( page=99999999, size=1)
	j_res = json.loads(response.text)
	if(j_res['code']==1):
		assert j_res['data']['page'] == 100
		assert j_res['data'] != ""

	else:
		assert j_res['code'] == 20000
		assert j_res['err'] != ""

	assert j_res['msg'] != ""

