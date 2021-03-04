import requests
from lxml import etree
from bs4 import BeautifulSoup
from flask import jsonify, request
import json
import re

def login(uid, pwd):
  session= requests.session()
  req = session.get("https://as2.npu.edu.tw/npu/index.html")
  print("Session GET....")
  payload = {
    "uid": uid,
    "pwd": pwd
  }
  needreturn = []
  session = session.post("https://as2.npu.edu.tw/npu/perchk.jsp",data=payload,timeout=5)
  print("Account Login....")
  data = etree.HTML(session.text)
  try:
    is_login = data.xpath("/html/body/script")[0].text.find('不正確')
    if is_login >= 0 :
      pld = {'stdid': 'fail'}
      needreturn.append(pld)
      print("Login Fail....")
      return json.dumps(needreturn)
  except Exception as error:
    soup = BeautifulSoup(session.text, 'html.parser')
    value = soup.find('input', {'pld': 'std_id1'}).get("value")
    pld = {'stdid': value }
    print("Login!!")
    needreturn.append(pld)
    return json.dumps(needreturn)