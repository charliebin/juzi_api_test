from lib.api_call_functions import *
import pytest
import json
import time

def test_get_article_get_with_empty_id():
    response = get_article_get(id=0)
    j_res = json.loads(response.text)
    #print response.text
    assert j_res['code'] == 10003
    assert j_res['msg'] != ""
    assert j_res['err'] != ""

def test_get_article_get_with_empty_id():
    response = get_article_get(id=0)
    j_res = json.loads(response.text)
    #print response.text
    assert j_res['code'] == 10003
    assert j_res['msg'] != ""
    assert j_res['err'] != ""
