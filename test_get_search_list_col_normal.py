#coding:utf-8
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json
def test_get_search_list_col_with_uid_and_keyword():
	#pdb.set_trace()
	response = get_search_list_col(10049,'范冰冰')
	j_res=json.loads(response.text)
	if j_res['code'] == 1:
		assert j_res['data'] != ""
		assert len(j_res['data']['list']) !=0
		assert j_res['data']['page'] != ""
