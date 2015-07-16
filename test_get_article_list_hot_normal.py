from lib.api_call_functions import *
import pytest
import json

def test_get_article_list_hot_default():
    response = get_article_list_hot()
    j_res = json.loads(response.text)

    assert j_res['code'] == 1
    assert j_res['msg'] != ""
    assert j_res['data'] != ""

