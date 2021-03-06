# coding=utf-8
import sys
sys.path.append("..")
from lib.api_call_functions import *
import pytest
import json

def test_get_article_list_hot_with_large_page_and_size():
    response = get_article_list_hot(ts=0, page=999, size=9999)
    #response = get_article_list_hot(ts=0, page=100, size=30)
    print response.text
    j_res = json.loads(response.text)

    assert j_res['code'] == 1
    assert j_res['msg'] != ""
    assert j_res['data'] != ""

def test_get_article_list_hot_with_minus_page_and_size():
    response = get_article_list_hot(ts=0, page=-1, size=-1)
    j_res = json.loads(response.text)
    print response.text

    assert j_res['code'] == 20000
    assert j_res['msg'] == u"橘子君找不到更多数据"
    assert j_res['err'] != ""
