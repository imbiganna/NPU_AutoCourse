import requests
from lxml import etree
from bs4 import BeautifulSoup
from flask import jsonify, request
import json
import re
import time
from fake_useragent import UserAgent
import random


def gogoCourse(cid,uid,pwd):
  session= requests.session()
  rd=random.randint(0,1)
  url = ['as1.npu.edu.tw','as2.npu.edu.tw']
  payload = {
      "uid": uid,
      "pwd": pwd
  }
  ua = UserAgent()
  user_agent = ua.random
  print(user_agent)
  ua = {
    'Host' : url[rd],
  	'user-agent' : user_agent,
  	'Origin': 'https://'+url[rd]
  }
  ret = []
  print('Login Session GET...')
  req = session.get("https://"+url[rd]+"/npu/index.html",headers=ua)
  r = session.post("https://"+url[rd]+"/npu/perchk.jsp", data=payload, timeout=5 ,headers=ua)
  print("Login Seccuss!!")

  print("GO Course...")
  cid = cid.replace('andcou','%')
  cids = cid.split('%')
  payload = {
      "content" : cid
  }
  i=0
  for courseid in cids:
      payload["check"+str(i)] = courseid
      i+=1

  ret = []
  try:
   time.sleep(0.3)
   r = session.post("https://"+url[rd]+"/npu/choice/0A00_ins.jsp",data=payload,timeout=5 ,headers=ua)
   print('DONE>>>')
   print(r.text)

   isDone = r.text.find('重複')
   if isDone > 0:
    sts = {'status': 'failDueRPT'}
    ret.append(sts)
   isDone = r.text.find('繁忙')
   if isDone > 0:
    sts = {'status': 'failDueBusy'}
    ret.append(sts)
   isDone = r.text.find('衝堂')
   if isDone > 0:
    sts = {'status': 'failDueBoom'}
    ret.append(sts)
   isDone = r.text.find('選上')
   if isDone > 0:
    sts = {'status': 'true'}
    ret.append(sts)
   elif isDone == -1:
    sts = {'status': 'fail'}
    ret.append(sts)

   print(ret)
   return json.dumps(ret)
  except:
   sts = {'status': 'fail'}
   ret.append(sts)
   return json.dumps(ret)