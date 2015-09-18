import sys
sys.path.append("..")
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json

def test_get_search_index():
	#pdb.set_trace()
	response = get_search_index()
	j_res=json.loads(response.text)
	assert response.status_code == 200
	assert j_res['code'] == 1
	assert j_res['data'] != ""
	assert len(j_res['data']['list'])!=0
