#coding:utf-8
import sys
sys.path.append("..")
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json
import time
from time import sleep
def test_post_comment_create():
	#pdb.set_trace()
	#aid列表
	articleID=[6166,6165,6164,6163,6162,6161,6160,6159,6158,6157]
	for i in range(0,len(articleID)):
		response = post_comment_create(uid=473451,aid=articleID[i])
		j_res = json.loads(response.text)
		assert response.status_code == 200
		assert j_res['code'] == 1
		time.sleep(10)
