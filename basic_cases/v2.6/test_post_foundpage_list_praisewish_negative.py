import sys
sys.path.append("..")
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json
import time
import pdb
def test_post_foundpage_list_praisewish():
       response = post_foundpage_list_praisewish(sid="",uid="",accesstoken="",wid="")
       j_res = json.loads(response.text)
       
       assert j_res['code'] == 10000
       assert j_res['msg'] != ""
       assert j_res['err']!=""


