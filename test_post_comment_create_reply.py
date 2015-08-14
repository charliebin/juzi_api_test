#coding:utf-8
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json
import time
def test_post_comment_create_reply():
	#pdb.set_trace()
	#aid列表
	articleID=[6166,6165,6164,6163,6162,6161,6160,6159,6158,6157]
	replyID=[818425,818426,818427,818428,818429,818430,818431,818432,818433,818434]
	for i in range(0,len(articleID)):
		response = post_comment_create_reply(uid=386615,replyid=replyID[i],aid=articleID[i])
		j_res = json.loads(response.text)
		assert response.status_code == 200
		assert j_res['code'] == 1
		time.sleep(10)
