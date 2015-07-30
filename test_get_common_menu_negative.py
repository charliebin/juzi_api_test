from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json
import time

def test_get_common_menu_with_unusal_uid():
	response = get_common_menu(uid='xy')
	j_res = json.loads(response.text)
	#print response.text
	assert j_res['code'] == 1
	assert j_res['msg'] != ""
	assert j_res['data'] != ""
def test_get_common_menu_with_minus_uid():
	response = get_common_menu(uid=-1)
	j_res = json.loads(response.text)
	#print response.text
	assert j_res['code'] == 1
	assert j_res['msg'] != ""
	assert j_res['data'] != ""
def test_get_common_menu_with_large_uid():
	response = get_common_menu(uid=1000000)
	j_res = json.loads(response.text)
	#print response.text
	assert j_res['code'] == 1
	assert j_res['msg'] != ""
	assert j_res['data'] != ""
