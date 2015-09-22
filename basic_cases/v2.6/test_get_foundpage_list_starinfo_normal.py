import sys
sys.path.append("..")
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json
import time
import pdb

def test_get_foundpage_list_starinfo_default1():
       response = get_foundpage_list_starinfo()
       j_res = json.loads(response.text)

       assert j_res['code'] == 1
       assert j_res['msg'] != ""
       assert j_res['data'] != ""
       assert j_res["data"]['ts'] != ""
       assert j_res["data"]['page'] != ""

def test_get_foundpage_list_starinfo_default2():
	response = get_foundpage_list_starinfo(sid="1",page=2)
	j_res = json.loads(response.text)

	assert j_res['code'] ==1
	assert j_res['msg']!=""
