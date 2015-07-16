from lib.api_call_functions import *
import pytest
import json
import time

def test_get_article_list_attitude_with_large_page_and_size():
    response = get_article_list_attitude(id=18, ts=time.time(), page=999, size=999)
    j_res = json.loads(response.text)

    assert j_res['code'] == 20000
    assert j_res['msg'] != ""
    assert j_res['err'] != ""

def test_get_article_list_attitude_with_not_existed_attitude():
    response = get_article_list_attitude(id=180, ts=time.time(), page=1, size=30)
    j_res = json.loads(response.text)

    assert j_res['code'] == 20000
    assert j_res['msg'] != ""
    assert j_res['err'] != ""

def test_get_article_list_attitude_with_minus_page_and_size():
    response = get_article_list_attitude(id=18, ts=time.time(), page=-1, size=-1)
    j_res = json.loads(response.text)

    assert j_res['code'] == 1
    assert j_res['msg'] != ""
    assert j_res['data'] != ""
