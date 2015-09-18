#coding:utf-8
import sys
sys.path.append("..")
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

def test_get_common_menu_with_uid():
        response = get_common_menu(uid=473451)
        j_res = json.loads(response.text)
        assert response.status_code == 200
        assert j_res['code'] == 1
        assert j_res['msg'] != ""
        assert j_res['data'] != ""

