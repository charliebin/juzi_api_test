import sys
sys.path.append("..")
from lib.api_call_functions import *
import pytest
import json

def test_get_article_list_home_default():
    #pdb.set_trace()
    response = get_article_list_home()
    j_res = json.loads(response.text)

    assert j_res['code'] == 1
    assert j_res['msg'] != ""
    assert j_res['data'] != ""

def test_get_article_list_home_with_uid():
    #pdb.set_trace()
    response = get_article_list_home("10094")
    j_res = json.loads(response.text)

    assert j_res['code'] == 1
    assert j_res['msg'] != ""
    assert j_res['data'] != ""
