import sys
sys.path.append("..")
from lib.api_call_functions import *
from lib.util_functions import *
import pytest
import json
import time
def test_get_article_content():
	response = get_article_content()
	#j_res = json.loads(response.text)
	assert response.status_code == 200
	#assert j_res['code'] == 1
	#assert j_res['msg'] != ""
	#assert j_res['data'] != ""
