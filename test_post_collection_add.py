#coding:utf-8
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json
import time
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
def test_post_collection_add():
	#pdb.set_trace()
	#ls=[4571,4672,4736,4814,4807,4867,4870,4918,4971,5163,5170,5166,2604,2558,2875,2870]
	ls=[4435,4388,4239,4242,4145,4139]
	for i in range(0,len(ls)):
		response = post_collection_add(10049,ls[i], md5_gen(10049))
		j_res = json.loads(response.text)
		assert response.status_code == 200
		assert j_res['code'] == 1
