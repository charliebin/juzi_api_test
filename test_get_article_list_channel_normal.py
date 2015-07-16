from lib.api_call_functions import *
import pytest
import json
import time

def test_get_article_list_channel_normal():
    response = get_article_list_channel(id=26, ts=time.time(), page=1, size=30)
    j_res = json.loads(response.text)

    assert j_res['code'] == 1
    assert j_res['msg'] != ""
    assert j_res['data'] != ""

