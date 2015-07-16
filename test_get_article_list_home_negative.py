from lib.api_call_functions import *
import pytest
import json

def test_get_article_list_home_with_large_size_and_page():
    '''
	even with large page and size parameter, api should handler correctly. 
    '''
    response = get_article_list_home(uid="10094", ts=0, page=999, size=999)
    j_res = json.loads(response.text)

    #there should be no data in that page
    assert j_res['code'] == 20000
    assert j_res['msg'] != ""
    assert j_res['err'] != ""

def test_get_article_list_home_with_minus_size_and_page():
    #what's the action of get_article_list_home when passing negative number in param 'size'.
    response = get_article_list_home(uid="10094", ts=0, page=-1, size=-1)
    j_res = json.loads(response.text)

    print response.text

    assert j_res['code'] == 1
    assert j_res['msg'] != ""
    assert j_res['data'] != ""
