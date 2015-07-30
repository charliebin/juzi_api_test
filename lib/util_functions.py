#coding:utf-8
import json
import requests
import time
import hashlib
import pdb
import random

#md5 encode generatioin, used in uid generation
def md5_gen(uid):
	return hashlib.md5((str(uid)+"+j3uzIyu7le0&aa").encode('utf-8')).hexdigest()

#random openid
def random_openid():
	return str(random.randint(19999999,59999999))

#random char, used to generate user name
def random_char():
	return random.choice('abcdefghijklmnopqrstuvwxyz')

if __name__ == "__main__":
	print random_char()
