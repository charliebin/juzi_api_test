from lib.api_call_functions import *
import pytest
import json
import time

def test_get_article_list_channel_wiht_minus_page_and_size():
    response = get_article_list_channel(id=260000, ts=time.time(), page=1, size=30)
    j_res = json.loads(response.text)

    assert j_res['code'] == 20000
    assert j_res['msg'] != ""
    assert j_res['err'] != ""

def test_get_article_list_channel_with_large_page_and_size():
    response = get_article_list_channel(id=26, ts=time.time(), page=999, size=999)
    j_res = json.loads(response.text)

    assert j_res['code'] == 20000
    assert j_res['msg'] != ""
    assert j_res['err'] != ""

def test_get_article_list_channel_with_minus_page_and_size():
    response = get_article_list_channel(id=26, ts=time.time(), page=-1, size=-1)
    j_res = json.loads(response.text)

    assert j_res['code'] == 1
    assert j_res['msg'] != ""
    assert j_res['data'] != ""
