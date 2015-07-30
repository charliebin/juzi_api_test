#coding:utf-8
from lib.api_call_functions import *

from lib.util_functions import *
import pytest
import json
import time

def test_get_common_menu_normal():
	response = get_common_menu()
	j_res = json.loads(response.text)
	assert response.status_code == 200
	assert j_res['code'] == 1
	assert j_res['msg'] != ""
	assert j_res['data'] != ""
	assert len(j_res['data'])==9
	if  j_res['data'][7]['name']=='心情':
		assert len(j_res['data'][7]['data'])==3
	if  j_res['data'][8]['name']=="精选栏目" :
		assert len(j_res['data'][8]['data'])==6
def test_get_common_menu_with_uid():
        response = get_common_menu(uid=473451)
        j_res = json.loads(response.text)
        assert response.status_code == 200
        assert j_res['code'] == 1
        assert j_res['msg'] != ""
        assert j_res['data'] != ""
        assert len(j_res['data'])==9
        if  j_res['data'][7]['name']=='心情':
                assert len(j_res['data'][7]['data'])==3
        if  j_res['data'][8]['name']=="精选栏目" :
                assert len(j_res['data'][8]['data'])==5

