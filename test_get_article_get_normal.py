from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json
import time
import pdb

def test_get_article_get_default():
   #pdb.set_trace()
    response = get_article_get()
    j_res = json.loads(response.text)
    
    assert j_res['code'] == 1
    assert j_res['msg'] != ""
    assert j_res['data'] != ""

