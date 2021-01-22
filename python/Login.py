import requests
from lxml import etree
from bs4 import BeautifulSoup
from flask import jsonify, request
import json
import re

def login(uid, pwd):
  session= requests.session()
  req = session.get("https://as2.npu.edu.tw/npu/index.html")
  payload = {
    "uid": uid,
    "pwd": pwd
  }
  ret = []
  r = session.post("https://as2.npu.edu.tw/npu/perchk.jsp",data=payload,timeout=5)

  root = etree.HTML(r.text)
  try:
    is_login = root.xpath("/html/body/script")[0].text.find('不正確')
    if is_login >= 0 :
      id = {'stdid': 'fail'}
      ret.append(id)
      return json.dumps(ret)
  except Exception as error:
    soup = BeautifulSoup(r.text, 'html.parser')
    value = soup.find('input', {'id': 'std_id1'}).get("value")
    id = {'stdid': value }
    ret.append(id)
    return json.dumps(ret)