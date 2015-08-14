#coding:utf-8
import json
import requests
import time
import hashlib
import pdb
import random
from util_functions import *

#hostname = "api.app.happyjuzi.com/v2.0"
#直接后端访问＋7001端口；访问varnish则不加端口；
hostname = "testapi.app.happyjuzi.com/v2.2"
#hostname = "123.57.10.208:7001/v2.2"
suffix = "&pf={pf}&net={net}&res={res}&ver={ver}"

port = ""

pf = "ios"
net = "4g"
res = "720x1184"
ver = "2.2"

if port == "":
	request_url_temp = "http://{hostname}/".format(hostname=hostname)
else:
	request_url_temp = "http://{hostname}:{port}/".format(hostname=hostname, port=port)

class TestResult():
    def __init__(self):
	self.result = "false"
	self.duration = -1
	self.id = 0

#Article operations
def get_comment_list_user(uid,page,size,sort):
	#pdb.set_trace()  
	hostname = "testapi.app.happyjuzi.com/v2.4"
	request_url_temp = "http://{hostname}/".format(hostname=hostname)
	pf = "android"
	net = "wifi"
	res = "720x1184"
	ver = "2.4"
	if uid=="" and page =="" and size =="" and sort =="":
		request_url = request_url_temp + "comment/list/user"
	elif uid!="" and page =="" and size =="" and sort =="":
		request_url = request_url_temp + "comment/list/user" + \
		"?uid={0}&ts={1}".format(uid, time.time()) + \
		suffix.format(pf=pf, net = net,res=res, ver=ver)
	elif uid!="" and page =="" and size =="" and sort!="":
		request_url = request_url_temp + "comment/list/user" + \
		"?uid={0}&ts={1}&sort={2}".format(uid, time.time(),sort) + \
		suffix.format(pf=pf, net = net,res=res, ver=ver)
	elif  uid!="" and page !="" and size=="" and sort =="":
		request_url = request_url_temp + "comment/list/user" + \
		"?uid={0}&ts={1}&page={2}&size={3}". \
			format(uid,time.time(),page,size) + \
		suffix.format(pf=pf, net = net,res=res, ver=ver)
	elif uid!="" and page !="" and size!="" and sort=="":
		request_url = request_url_temp + "comment/list/user" + \
		"?uid={0}&ts={1}&page={2}&size={3}". \
			format(uid,time.time(),page,size) + \
		suffix.format(pf=pf, net = net,res=res, ver=ver)
	elif uid!="" and page !="" and size!="" and sort !="":
		request_url = request_url_temp + "comment/list/user" + \
		"?uid={0}&ts={1}&page={2}&size={3}&sort={4}". \
			format(uid,time.time(),page,size,sort) + \
		suffix.format(pf=pf, net = net,res=res, ver=ver)

	time_start = time.time()
	t_result = TestResult()
	try:
	    resp = requests.get(request_url)
	except:
	    pass
	time_end = time.time()
	t_result.duration = time_end - time_start
	return resp
def post_subscribe_cancel(type,uid,id,accesstoken):
	#pdb.set_trace()
	hostname = "devapi.app.happyjuzi.com/v2.4"
	request_url_temp = "http://{hostname}/".format(hostname=hostname) 
	request_url = request_url_temp + "subscribe/cancel"
	time_start = time.time()
	parameter = {"type":type,"uid":uid,"id":id,"accesstoken":accesstoken}
	t_result = TestResult()
	try:
		 resp = requests.post(request_url, data=parameter)
        except:
		pass
	time_end = time.time()
	return resp    
def post_subscribe_add(type,uid,id,accesstoken ):
	#pdb.set_trace()
	hostname = "devapi.app.happyjuzi.com/v2.4"
	request_url_temp = "http://{hostname}/".format(hostname=hostname) 
	request_url = request_url_temp + "subscribe/add"
	time_start = time.time()
	parameter = {"type":type,"uid":uid,"id":id,"accesstoken":accesstoken}
	try:
		 resp = requests.post(request_url, data=parameter)
        except:
		pass
	time_end = time.time()
	return resp    
def get_common_setting(uid=""):
	#pdb.set_trace()
	hostname = "testapi.app.happyjuzi.com/v2.4"
	request_url_temp = "http://{hostname}/".format(hostname=hostname)
	pf = "android"
	net = "wifi"
	res = "720x1184"
	ver = "2.4"	
	if uid == "":
		request_url = request_url_temp + "common/setting"
	else:
		request_url = request_url_temp + "common/setting" + \
		"?uid={0}".format(uid) + \
		suffix.format(pf=pf, net = net,res=res, ver=ver)
	t_result = TestResult()
	time_start = time.time()
	try:
	    resp = requests.get(request_url)
	except:
	    pass
	time_end = time.time()
	t_result.duration = time_end - time_start
	return resp
def get_search_list_col(uid="",keyword="",page=1,size=30):
	#pdb.set_trace()
	hostname = "devapi.app.happyjuzi.com/v2.3"
	request_url_temp = "http://{hostname}/".format(hostname=hostname)
	pf = "android"
	net = "wifi"
	res = "720x1184"
	ver = "2.3"	
	if uid == "" and keyword == "":
		request_url = request_url_temp + "search/list/col"
	elif uid=="" and keyword !="":
		request_url = request_url_temp + "search/list/col" + \
		"?accesstoken={0}&ts={1}&keyword={2}". \
			format(md5_gen(uid), time.time(), keyword) + \
		suffix.format(pf=pf, net = net,res=res, ver=ver)
	elif uid!="" and keyword =="":
		request_url = request_url_temp + "search/list/col" + \
		"?accesstoken={0}&ts={1}&uid={2}". \
			format(md5_gen(uid), time.time(), uid) + \
		suffix.format(pf=pf, net = net,res=res, ver=ver)
	elif  uid!="" and keyword!="" :
		request_url = request_url_temp + "search/list/col" + \
		"?accesstoken={0}&ts={1}&uid={2}&keyword={3}&page={4}&size={5}". \
			format(md5_gen(uid),time.time(),uid,keyword,page,size) + \
		suffix.format(pf=pf, net = net,res=res, ver=ver)

	time_start = time.time()
	t_result = TestResult()
	try:
	    resp = requests.get(request_url)
	except:
	    pass

	time_end = time.time()
	t_result.duration = time_end - time_start
	return resp
def get_search_list_article(uid="",keyword="",page=1,size=30):
	#pdb.set_trace()
	hostname = "devapi.app.happyjuzi.com/v2.3"
	request_url_temp = "http://{hostname}/".format(hostname=hostname)
	pf = "android"
	net = "wifi"
	res = "720x1184"
	ver = "2.3"	
	if uid == "" and keyword == "":
		request_url = request_url_temp + "search/list/article"
	elif uid=="" and keyword !="":
		request_url = request_url_temp + "search/list/article" + \
		"?accesstoken={0}&ts={1}&keyword={2}&page={3}&size={4}". \
			format(md5_gen(uid), time.time(), keyword,page,size) + \
		suffix.format(pf=pf, net = net,res=res, ver=ver)
	elif uid!="" and keyword =="":
		request_url = request_url_temp + "search/list/col" + \
                  "?accesstoken={0}&ts={1}&uid={2}". \
                          format(md5_gen(uid), time.time(), uid) + \
                 suffix.format(pf=pf, net = net,res=res, ver=ver)
	elif  uid!="" and keyword!="" :
		request_url = request_url_temp + "search/list/article" + \
		"?accesstoken={0}&ts={1}&uid={2}&keyword={3}&page={4}&size={5}". \
			format(md5_gen(uid),time.time(),uid,keyword,page,size) + \
		suffix.format(pf=pf, net = net,res=res, ver=ver)

	time_start = time.time()
	t_result = TestResult()
	try:
	    resp = requests.get(request_url)
	except:
	    pass

	time_end = time.time()
	t_result.duration = time_end - time_start
	return resp
	
def get_search_list(uid="",keyword=""):
	#pdb.set_trace()
	hostname = "devapi.app.happyjuzi.com/v2.3"
	request_url_temp = "http://{hostname}/".format(hostname=hostname)
	pf = "android"
	net = "wifi"
	res = "720x1184"
	ver = "2.3"	
	if uid == "" and keyword == "":
		request_url = request_url_temp + "search/list"
	elif uid=="" and keyword !="":
		request_url = request_url_temp + "search/list" + \
		"?ts={0}&keyword={1}". \
			format(time.time(),keyword) + \
		suffix.format(pf=pf, net = net,res=res, ver=ver)
		print request_url
		print keyword
	elif uid!="" and keyword =="":
		 request_url = request_url_temp + "search/list" + \
                 "?accesstoken={0}&ts={1}&uid={2}". \
                         format(md5_gen(uid), time.time(), uid) + \
                 suffix.format(pf=pf, net = net,res=res, ver=ver)
	elif uid!="" and keyword!="":
		request_url = request_url_temp + "search/list" + \
		"?accesstoken={0}&ts={1}&uid={2}&keyword={3}". \
			format(md5_gen(uid),time.time(),uid,keyword) + \
		suffix.format(pf=pf, net = net,res=res, ver=ver)
		print keyword
	time_start = time.time()
	t_result = TestResult()
	try:
		resp = requests.get(request_url)
	except:
		pass
	time_end = time.time()
	t_result.duration = time_end - time_start
	return resp	

def get_search_index(uid=""):
	#pdb.set_trace()
	hostname = "devapi.app.happyjuzi.com/v2.3"
	request_url_temp = "http://{hostname}/".format(hostname=hostname)
	pf = "android"
	net = "wifi"
	res = "720x1184"
	ver = "2.3"	
	ts=time.time()
	if uid == "":
		request_url = request_url_temp + "search/index"
	else:
		request_url = request_url_temp + "search/index" + \
		"?accesstoken={token}&ts={ts}&uid={uid}". \
			format(token=md5_gen(uid), ts=ts,uid=uid) + \
		suffix.format(pf=pf, net = net,res=res, ver=ver)

	time_start = time.time()
	t_result = TestResult()
	try:
		resp = requests.get(request_url)
	except:
		pass
	time_end = time.time()
	t_result.duration = time_end - time_start
	return resp	

 
def post_collection_add(uid,aid,accesstoken ):
	#pdb.set_trace()
	hostname = "devapi.app.happyjuzi.com/v2.3"
	request_url_temp = "http://{hostname}/".format(hostname=hostname) 
	request_url = request_url_temp + "collection/add"
	time_start = time.time()
	parameter = {"uid":uid,"aid":aid,"accesstoken":accesstoken}
	try:
		 resp = requests.post(request_url, data=parameter)
        except:
		pass
	time_end = time.time()
	return resp    
def get_collection_list_video(uid="",ts=time.time(),page=1,size=30):
	#pdb.set_trace()
	hostname = "devapi.app.happyjuzi.com/v2.3"
	request_url_temp = "http://{hostname}/".format(hostname=hostname)
	pf = "android"
	net = "wifi"
	res = "720x1184"
	ver = "2.3"	
	if uid == "":
		request_url = request_url_temp + "collection/list/video"
	else:
		request_url = request_url_temp + "collection/list/video" + \
		"?accesstoken={token}&ts={ts}&page={page}&size={size}&uid={uid}". \
			format(token=md5_gen(uid), ts=ts, page=page, size=size, uid=uid) + \
		suffix.format(pf=pf, net = net,res=res, ver=ver)

	time_start = time.time()
	t_result = TestResult()
	try:
		resp = requests.get(request_url)
	except:
		pass
	time_end = time.time()
	t_result.duration = time_end - time_start
	return resp	

def get_common_menu(uid="",ts=time.time()):

	# pdb.set_trace()
	hostname = "devapi.app.happyjuzi.com/v2.3"
	request_url_temp = "http://{0}/".format(hostname)
	pf = "android"
	net = "wifi"
	res = "720x1184"
	ver = "2.3"
	if uid=="":
		request_url = request_url_temp + "common/menu" + \
                "?"+suffix.format(pf=pf, net = net,res=res, ver=ver)
	else:
		request_url = request_url_temp + "common/menu" + \
                "?accesstoken={0}&ts={1}&uid={2}". \
                format(md5_gen(uid), ts,uid) + \
                suffix.format(pf=pf, net = net,res=res, ver=ver)
	time_start = time.time()
	t_result = TestResult()
	try:
		resp = requests.get(request_url)
	except:
		pass

	time_end = time.time()

	t_result.duration = time_end - time_start

	return resp
	
def get_article_list_video(uid='',ts=time.time(),page=1,size=30):
	# pdb.set_trace()
	hostname = "devapi.app.happyjuzi.com/v2.3"
	request_url_temp = "http://{0}/".format(hostname)
	pf = "android"
	net = "wifi"
	res = "720x1184"
	ver = "2.3"
	if uid=="":
		request_url = request_url_temp + "article/list/video" + \
		"?accesstoken={0}&ts={1}&page={2}&size={3}". \
		 format(md5_gen(uid), ts, page,size) + \
		 suffix.format(pf=pf, net = net,res=res, ver=ver)
	elif uid!="":
		request_url = request_url_temp + "article/list/video" + \
		"?accesstoken={0}&ts={1}&page={2}&size={3}&uid={4}". \
		format(md5_gen(uid), ts, page,size,uid) + \
		suffix.format(pf=pf, net = net,res=res, ver=ver)
	time_start = time.time()
	t_result = TestResult()
	try:
		resp = requests.get(request_url)
		#t_result.result = "true"
	except:
        #t_result.result = "false"
		pass

	time_end = time.time()

	t_result.duration = time_end - time_start

	return resp	
def get_article_list_home(uid="", ts=0,page=2,size=30):

	#pdb.set_trace()
	if ts == 0:
		ts = time.time()
	
	if uid == "":
		request_url = request_url_temp + "article/list/home"
	else:
		request_url = request_url_temp + "article/list/home" + \
		"?accesstoken={token}&ts={ts}&page={page}&size={size}&uid={uid}". \
		format(token=md5_gen(uid), ts=ts, page=page, size=size, uid=uid) + \
		suffix.format(pf=pf, net = net,res=res, ver=ver)
	
	time_start = time.time()
	t_result = TestResult()
	
	try:
		resp = requests.get(request_url)	
		#t_result.result = "true"
	except:
		#t_result.result = "false"
		pass
	
	time_end = time.time()
	
	t_result.duration = time_end - time_start
	
	return resp

def get_article_list_newhome(uid='',ts=0,page=1,size=30):
        #pdb.set_trace()
	hostname = "testapi.app.happyjuzi.com/v2.3"
	request_url_temp = "http://{hostname}/".format(hostname=hostname)
	pf = "android"
	net = "wifi"
	res = "720x1184"
	ver = "2.3"	

        if ts == 0:
                ts = time.time()

        if uid == "":
                request_url = request_url_temp + "article/list/home?page={0}&size={1}".format(page,size)
        else:
                request_url = request_url_temp + "article/list/home" + \
                "?accesstoken={token}&ts={ts}&page={page}&size={size}&uid={uid}". \
                format(token=md5_gen(uid), ts=ts, page=page, size=size, uid=uid) + \
                suffix.format(pf=pf, net = net,res=res, ver=ver)
	
        time_start = time.time()
	
        t_result = TestResult()

        try:
                resp = requests.get(request_url)
                #t_result.result = "true"
        except:
                #t_result.result = "false"
                pass

        time_end = time.time()

        t_result.duration = time_end - time_start

        return resp	


def get_article_list_hot(ts=0,page=1,size=30):
	#pdb.set_trace()
	if ts == 0:
		ts = time.time()
		
	request_url = request_url_temp + "article/list/hot" + \
	"?ts={ts}&page={page}&size={size}".format(ts=ts, page=page, size=size) + \
	suffix.format(pf=pf, net = net,res=res, ver=ver)
	
	time_start = time.time()
	
	try:
		resp = requests.get(request_url)	
	except:
		return none
	
	return resp

def get_article_list_recommend(ts=0,page=1,size=30):
	#pdb.set_trace()
	if ts == 0:
		ts = time.time()
	
	request_url = request_url_temp + "article/list/recommend" + \
	"?ts={ts}&page={page}&size={size}".format(ts=ts, page=page, size=size) + \
	suffix.format(pf=pf, net = net,res=res, ver=ver)

	time_start = time.time()
	try:
		resp = requests.get(request_url)
	except:
		return none
	
	return resp

def get_article_list_channel(id=26,ts=0,page=1,size=30):
	#pdb.set_trace()
	if ts == 0:
		ts = time.time()
	
	request_url = request_url_temp + "article/list/channel" + \
	"?id={id}&ts={ts}&page={page}&size={size}".format(id=id, ts=ts, page=page, size=size)\
	 + suffix.format(pf=pf, net = net,res=res, ver=ver)
	
	time_start = time.time()
	try:
		resp = requests.get(request_url)
	except:
		return none
	
	return resp
def get_article_list_newchannel(id='',ts=time.time(),page=1,size=30):
	#pdb.set_trace()
	hostname = "devapi.app.happyjuzi.com/v2.3"
	request_url_temp = "http://{0}/".format(hostname)
	pf = "android"
	net = "wifi"
	res = "720x1184"
	ver = "2.3"	
	if id=='':
		request_url = request_url_temp + "article/list/channel" + \
		"?ts={ts}&page={page}&size={size}".format(ts=ts, page=page, size=size)\
		+ suffix.format(pf=pf, net = net,res=res, ver=ver)
	else:
		request_url = request_url_temp + "article/list/channel" + \
		"?id={id}&ts={ts}&page={page}&size={size}".format(id=id, ts=ts, page=page, size=size)\
		+ suffix.format(pf=pf, net = net,res=res, ver=ver)
	
	time_start = time.time()
	t_result = TestResult()

	try:
		resp = requests.get(request_url)
	except:
		return none
	
	time_end = time.time()
	t_result.duration = time_end - time_start
	return resp
	
def get_article_list_category(id=26,ts=0,page=1,size=30):
	return get_article_list_channel(id=26,ts=0,page=1,size=30)
	
	
def get_article_list_attitude(id=18,ts=0,page=1,size=30):
	#pdb.set_trace()
	if ts == 0:
		ts = time.time()
	request_url = request_url_temp + "article/list/attitude" + \
		"?id={id}&ts={ts}&page={page}&size={size}".format(id=id, ts=ts, page=page, size=size)\
		+ suffix.format(pf=pf, net = net,res=res, ver=ver)
	time_start = time.time()
	try:
		resp = requests.get(request_url)
	except:
		return none	
	return resp
	
def get_article_list_author(id=17,ts=0,page=1,size=30):
	#pdb.set_trace()
	if ts == 0:
		ts = time.time()
	request_url = request_url_temp + "article/list/author" + \
		"?id={id}&ts={ts}&page={page}&size={size}".format(id=id, ts=ts, page=page, size=size) + \
		suffix.format(pf=pf, net = net,res=res, ver=ver)

	try:
		resp = requests.get(request_url)
	except:
		return none

	return resp
	
def get_article_list_tag(ts=0,page=1,size=30):
	#pdb.set_trace()
	if ts == 0:
		ts = time.time()
	request_url = request_url_temp + "article/list/tag" + \
		"?ts={ts}&page={page}&size={size}".format(ts=ts, page=page, size=size) + \
		suffix.format(pf=pf, net = net,res=res, ver=ver)

	time_start = time.time()
	t_result = TestResult()
	try:
		resp = requests.get(request_url)
		
		t_result.result = "true"
	except:
		t_result.result = "false"
	
	time_end = time.time()
	
	t_result.duration = time_end - time_start
	
	return t_result
	
def get_article_get(id=3983):
	#pdb.set_trace()
	request_url = request_url_temp + "article/get?id={id}".format(id=id) + \
	suffix.format(pf=pf, net = net,res=res, ver=ver)
	
        try:
		resp = requests.get(request_url)
	except:
		return none
	
	return resp
	
def get_article_content(id=4371):
    #pdb.set_trace()
	request_url = request_url_temp + "article/content?id={id}".format(id=id)
	time_start = time.time()
	t_result = TestResult()
	try:
		resp = requests.get(request_url)
		t_result.result = "true"
	except:
		t_result.result = "false"
	
	time_end = time.time()
	
	t_result.duration = time_end - time_start
	
	return t_result
	
def get_article_sharestats(channel="baidu", id=4403, sto="WEIXIN_CIRCLE"):
	#pdb.set_trace()
	request_url = request_url_temp + \
	"article/sharestats?channel={channel}&id={id}&sto={sto}".format(channel=channel, \
	id=id, sto=sto)
	time_start = time.time()
	t_result = TestResult()
	try:
		resp = requests.get(request_url)
		
		t_result.result = "true"
	except:
		t_result.result = "false"
	
	time_end = time.time()
	
	t_result.duration = time_end - time_start
	
	return t_result

#User operations
def get_user_info(uid="17775"):
	#pdb.set_trace()
	request_url = request_url_temp + "user/info?uid={uid}".format(uid=uid)
		
	time_start = time.time()
	t_result = TestResult()
	try:
		resp = requests.get(request_url)
		t_result.result = "true"
	except:
		t_result.result = "false"
	
	time_end = time.time()
	
	t_result.duration = time_end - time_start
	
	return t_result

def create_user(openid, username):
	#pdb.set_trace()
	
	userinfo = { 
	"openid":str(openid),
	"username": str(username),
	"avatar":"http:\/\/tp1.sinaimg.cn\/2167844952\/180\/5704907839\/1",
	"from":"sina",
	"sex" : "男"
	}
	
	j_userinfo = json.dumps(userinfo)
	
	accesstoken = md5_gen(openid)
	
	#data = { "userinfo":userinfo, "accesstoken":accesstoken}
	
	request_url = request_url_temp + "user/create"
	#+ suffix.format(pf=pf, net = net,rs=rs, ver=ver)
	
	time_start = time.time()
	t_result = TestResult()
	parameter = {'userinfo':j_userinfo, 'accesstoken': accesstoken, 'pf':'ios', 'ver':'v2.0'}
	
	try:
		resp = requests.post(request_url, data=parameter)
		
		t_result.result = "true"
		
	except:
		t_result.result = "false"
	
	time_end = time.time()
	
	t_result.duration = time_end - time_start
	
	return t_result
	
def potrait_user():
	pass

def update_user(userid, username):
	uid = userid
	sex = "男"
	birthday = "1980-00-00"
	nickname = username
	avatar = "http://qzapp.qlogo.cn/qzapp/101041134/C2073031D237B7FEB8E4A7A0D96D6593/100"
	accesstoken = md5_gen(userid)

	request_url = request_url_temp + "user/update"
	
	time_start = time.time()
	t_result = TestResult()
	parameter = {'uid':uid, 'sex': '男', 'birthday':birthday, 'nickname': nickname, \
	'avatar': avatar, 'accesstoken' : accesstoken, 'pf': 'ios', 'ver': 'v2.0'}
	
	try:
		resp = requests.post(request_url, data=parameter)
		t_result.result = "true"
		
	except:
		t_result.result = "false"
	
	time_end = time.time()
	
	t_result.duration = time_end - time_start
	
	return t_result
	
def update_clientid(clientid="462923850fc5bd957dd86b543a9de17f", uid="10115", ver="2.1.0.2", d_os="android"):
	clientid = clientid
	uid = uid
	ver = ver
	d_os = d_os
	accesstoken = md5_gen(uid)
	
	request_url = request_url_temp + "user/clientid/update"
	
	time_start = time.time()
	t_result = TestResult()
	parameter = {'uid': uid, 'clientid': clientid, 'd_os':d_os, 'ver': ver , 'accesstoken': accesstoken, 'pf':'android'}
	
	try:
		resp = requests.post(request_url, data=parameter)
		t_result.result = "true"
	except:
		t_result.result = "false"
	
	time_end = time.time()
	
	t_result.duration = time_end - time_start
	
	return t_result

def check_user(uid="100095", nickname="Testabc"):
	uid = uid
	nickname = nickname
	accesstoken = md5_gen(uid)
	
	request_url = request_url_temp + "user/check"
	
	time_start = time.time()
	t_result = TestResult()
	parameter = {'uid': uid, 'nickname': nickname, 'accesstoken': accesstoken, 'pf':'android'}
	
	try:
		resp = requests.post(request_url, data=parameter)
		t_result.result = "true"
	except:
		t_result.result = "false"
	
	time_end = time.time()
	
	t_result.duration = time_end - time_start
	
	return t_result

#Comment operatoins
def get_comment_list(ts=0,page=1,size=30):
	if ts == 0:
		ts = time.time()
	request_url = request_url_temp + "comment/list" + "?ts={ts}&page={page}".format(ts=ts,page=page)
	time_start = time.time()
	t_result = TestResult()
	try:
		resp = requests.get(request_url)
		t_result.result = "true"
	except:
		t_result.result = "false"
	time_end = time.time()
	t_result.duration = time_end - time_start
	return t_result

def get_attitude_get(id=20):
	request_url = request_url_temp + "attitude/get"+"?id={id}".format(id=id)
	time_start = time.time()
	t_result = TestResult()
	try:
		resp = requests.get(request_url)
		t_result.result = "true"
	except:
		t_result.result = "false"
	time_end = time.time()
	t_result.duration = time_end - time_start
	return t_result

#Common operations


def post_comment_create(uid='',aid=''):
	#pdb.set_trace()
	hostname = "testapi.app.happyjuzi.com/v2.4"
	request_url_temp = "http://{hostname}/".format(hostname=hostname)
	pf = "android"
	net = "wifi"
	res = "720x1184"
	ver = "2.0"
	request_url = request_url_temp + "comment/create"
	time_start = time.time()
	t_result = TestResult()
	try:
		commands ={
		'uid':uid,
		'aid':aid,           
		'content':"这篇文章不错啊！",
		'accesstoken':md5_gen(uid),
		}
		resp = requests.post(request_url,data=commands)
		t_result.result = "true"
	except:
		t_result.result = "false"
	time_end = time.time()
	t_result.duration = time_end - time_start
	return resp 

def post_comment_create_reply(uid='',replyid='',aid=''):
	hostname = "testapi.app.happyjuzi.com/v2.4"
	request_url_temp = "http://{hostname}/".format(hostname=hostname)
	pf = "android"
	net = "wifi"
	res = "720x1184"
	ver = "2.0"
	request_url = request_url_temp + "comment/create"
	time_start = time.time()
	t_result = TestResult()
	try:
		commands ={
		'uid':uid,
		'aid':aid,
		'replyid':replyid,                     
		'content':'reply to mujia!',
		'accesstoken':md5_gen(uid),
		}
		resp = requests.post(request_url,data=commands)
		t_result.result = "true"
	except:
		t_result.result = "false"
	time_end = time.time()
	t_result.duration = time_end - time_start
	return resp   
def post_comment_complaint(uid,id):
	request_url = request_url_temp + "comment/complaint"
	time_start = time.time()
	t_result = TestResult()
	try:
		commands ={
		'uid':uid,
		'id':id,
		'accesstoken':md5_gen(uid),
		}
		resp = requests.post(request_url,data=commands)

		t_result.result = "true"
	except:
		t_result.result = "false"

	print resp.content
	time_end = time.time()

	t_result.duration = time_end - time_start

	return t_result

def post_comment_destroy(uid,id,aid):
	request_url = request_url_temp + "comment/destroy"
	time_start = time.time()
	t_result = TestResult()

	try:
		commands ={
		'uid':uid,
		'id':id,
		'aid':aid,
		'accesstoken':md5_gen(uid),
		}
		resp = requests.post(request_url,data=commands)

		t_result.result = "true"
	except:
		t_result.result = "false"
	#print resp.content

	time_end = time.time()

	t_result.duration = time_end - time_start

	return t_result

#Attitude operations
def post_attitude_submit(uid="10094",id="15",aid="4424"):
	request_url = request_url_temp + "attitude/submit"
	time_start = time.time()
	t_result = TestResult()
	try:
		commands ={
		'uid':uid,
		'id':id,
		'aid':aid,
		'accesstoken':md5_gen(uid),
		}
		resp = requests.post(request_url,data=commands)

		t_result.result = "true"
	except:
		t_result.result = "false"
	#print resp.content
	time_end = time.time()

	t_result.duration = time_end - time_start
	return t_result

#if __name__ == "__main__":
