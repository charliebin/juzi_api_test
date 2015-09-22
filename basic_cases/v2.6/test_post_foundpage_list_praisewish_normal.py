import sys
sys.path.append("..")
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json
import time
import pdb
def test_post_foundpage_list_praisewish():
       response = post_foundpage_list_praisewish()
       j_res = json.loads(response.text)
       
       assert j_res['code'] == 1 or 30003
       assert j_res['msg'] != ""


