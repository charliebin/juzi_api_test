from lib.api_call_functions import *
import pytest
import json

def test_get_article_list_recommend_with_large_page_size():
    response = get_article_list_recommend(ts=0, page=999, size=999)
    j_res = json.loads(response.text)

    assert j_res['code'] == 1
    assert j_res['msg'] != ""
    assert j_res['data'] != ""

def test_get_article_list_recommend_with_minus_page_size():
    response = get_article_list_recommend(ts=0, page=-1, size=-1)
    j_res = json.loads(response.text)

    assert j_res['code'] == 1
    assert j_res['msg'] != ""
    assert j_res['data'] != ""
