#coding:utf-8
import json
import requests
import time
import hashlib
import pdb
import random
from lib.api_call_functions import *
from lib.util_functions import *
def test_post_collection_add(userid,aid):
	#hostname = "testapi.app.happyjuzi.com/v2.2"
	request_url_temp = "http://{0}/".format(hostname)
	uid = userid
	accesstoken = md5_gen(uid)

	request_url = request_url_temp + "collection/add"
	
	time_start = time.time()
	t_result = TestResult()
	parameter = {'uid':uid,'accesstoken' : accesstoken, 'aid':aid}
	
	try:
		resp = requests.post(request_url, data=parameter)
		t_result.result = "true"
		
	except:
		t_result.result = "false"
	
	time_end = time.time()
	
	t_result.duration = time_end - time_start
	
	return t_result
if __name__ == "__main__":
	print( collection_add(10049,2574))
