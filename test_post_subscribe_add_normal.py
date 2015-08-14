#coding:utf-8
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json
import time
def test_post_subscribe_add():
	#pdb.set_trace()
	ls=[49,57]
	for i in range(0,len(ls)):
		response = post_subscribe_add(3,473451,ls[i], md5_gen(473451))
		j_res = json.loads(response.text)
		assert response.status_code == 200
		assert j_res['code'] == 1
		request_url = "http://devapi.app.happyjuzi.com/v2.4/article/list/category?uid=473451&id={0}".format(ls[i])
		resp = requests.get(request_url)
		j_resp = json.loads(resp.text)
		assert j_resp['code'] == 1
		assert j_resp['data']['info']['issub'] == True
		print 'add success!'

