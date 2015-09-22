import sys
sys.path.append("..")
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json
import time
import pdb

def test_get_foundpage_list_starlist_default():
   #pdb.set_trace()
    response = get_foundpage_list_starlist()
    j_res = json.loads(response.text)
    
    assert j_res['code'] == 1
    assert j_res['msg'] != ""
    assert j_res['data'] != ""
    assert j_res["data"]['ts'] != ""
    assert j_res["data"]['page'] != ""

