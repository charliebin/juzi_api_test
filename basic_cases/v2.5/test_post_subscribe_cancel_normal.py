#coding:utf-8
import sys
sys.path.append("..")
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json
import time
def test_post_subscribe_cancel():
	#pdb.set_trace()
	ls=[49,57,72,73,53,54,55,56,58]
	for i in range(0,len(ls)):
		post_subscribe_add(3,473451, ls[i], md5_gen(473451))
		response = post_subscribe_cancel(3,473451,ls[i], md5_gen(473451))
		j_res = json.loads(response.text)
		assert response.status_code == 200
		assert j_res['code'] == 1
		
