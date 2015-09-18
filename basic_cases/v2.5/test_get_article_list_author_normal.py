from lib.api_call_functions import *
import pytest
import json
import time

def test_get_article_list_author_normal():
    response = get_article_list_author()
    j_res = json.loads(response.text)
    #print response.text
    assert j_res['code'] == 1
    assert j_res['msg'] != ""
    assert j_res['data'] != ""

