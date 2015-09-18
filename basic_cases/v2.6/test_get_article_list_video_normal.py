import sys
sys.path.append("..")
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json
import time

def test_get_article_list_video_normal():
	response = get_article_list_video()
	j_res = json.loads(response.text)
	assert response.status_code == 200
	assert j_res['code'] == 1
	assert j_res['msg'] != ""
	assert j_res['data'] != ""
	assert j_res['data']['page'] == 1


def test_get_article_list_video_with_uid_and_page():
	#pdb.set_trace()
	response = get_article_list_video(uid=473451,page=2 )
	j_res = json.loads(response.text)
	assert response.status_code == 200
	if( j_res['code']==1):
		assert j_res['data']['page'] == 2
		assert j_res['data'] != ""
		assert j_res['msg'] != ""
	else:
		assert j_res['code'] == 20000

