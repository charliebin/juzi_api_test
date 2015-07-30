from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json
def  test_get_collection_list_video_without_uid():
	response = get_collection_list_video()
	j_res = json.loads(response.text)
	#print response.text
	assert j_res['code'] == 10003
	assert j_res['msg'] != ""
	assert j_res['err'] != ""

def  test_get_collection_list_video_with_large_uid():
        response = get_collection_list_video(100000000)
        j_res = json.loads(response.text)
        #print response.text
        assert j_res['code'] == 20000
        assert j_res['msg'] != ""
        assert j_res['err'] != ""

def  test_get_collection_list_video_with_unusal_uid():
	response = get_collection_list_video("abcd")
	j_res = json.loads(response.text)
	#print response.text
	assert j_res['code'] == 10003
	assert j_res['msg'] != ""
	assert j_res['err'] != ""

def  test_get_collection_list_video_with_large_size_and_page():
	'''
	even with large page and size parameter, api should handler correctly.
	'''
	response = get_collection_list_video(uid=473451,page=999, size=999)
	assert response.status_code == 200
	j_res = json.loads(response.text)
	assert j_res['code'] == 20000
	assert j_res['msg'] != ""
	assert j_res['err'] != ""
def  test_get_collection_list_video_with_unusal_size_and_page():
	response =get_collection_list_video(uid=473451,page=-1, size=-1)
	j_res = json.loads(response.text)
	#print response.text
	assert j_res['code'] == 1
	assert j_res['msg'] != ""
	assert j_res['data'] != ""
	assert j_res['data']['page'] !=-1
def test_get_collection_list_video_with_page_and_minus_size():
        #pdb.set_trace()
        response = get_collection_list_video(uid=473451,page=10,size=1)
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

def  test_get_collection_list_video_with_minus_size_and_large_page():
	response = get_collection_list_video(uid=473451,page=99999999, size=1)
	j_res = json.loads(response.text)
	#print response.text
	if(j_res['code'] == 1):
		assert j_res['data']['page'] ==50
		assert j_res['data'] != ""
	else:
		assert j_res['code'] == 20000
		assert j_res['err'] != ""
	assert j_res['msg'] != ""

def  test_get_collection_list_video_with_unusal_size_and_page():
	response = get_collection_list_video(uid=473451,page='xy', size='xy')
	j_res = json.loads(response.text)
	#print response.text
	assert j_res['code'] == 1
	assert j_res['msg'] != ""
	assert j_res['data'] != ""
	assert j_res['data']['page'] != 'xy'

