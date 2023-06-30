# -*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import joblib
import numpy as np
import math
import os
from collections import Counter

lu='...'

pro=[]

for i1 in os.listdir(lu):
  w1=lu+i1+'/'
  for i2 in os.listdir(w1):
    w2=w1+i2+'/'
    print(w2)
    for i3 in os.listdir(w2):
      w3=w2+i3
      p=pd.read_csv(w3)
      pro.extend(np.ravel(p['frame.protocols']).tolist())
      l2=set(pro)
      pro=list(l2)


pro=['eth:ethertype:ip:udp:ssdp', 'eth:ethertype:ip:tcp:tls:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509ce:tls:x509ce:x509ce:pkix1implicit:x509ce:x509ce:pkix1explicit:x509ce:x509ce:x509ce:tls', 'eth:ethertype:ip:icmp:ip:udp', 'eth:ethertype:ip:udp:sip:sdp', 'eth:ethertype:ip:tcp:tls:x509sat:x509sat:x509ce', 'eth:ethertype:ip:udp:sip', 'eth:ethertype:ip:icmp:ip:udp:classicstun', 'eth:ethertype:ip:icmp', 'eth:ethertype:ip:udp:acdr', 'eth:ethertype:ip:udp:snmp:snmp', 'eth:ethertype:ip:udp', 'eth:ethertype:ip:udp:find', 'eth:ethertype:ip:udp:memcache', 'eth:ethertype:ip:udp:bfd', 'eth:ethertype:ip:udp:data', 'eth:ethertype:ip:tcp:http:data-text-lines', 'eth:ethertype:ip:icmp:ip:udp:cldap', 'eth:ethertype:ip:udp:rip', 'eth:ethertype:ip:udp:snmp:snmp:snmp', 'eth:ethertype:ip:icmp:ip:udp:data', 'eth:ethertype:ip:udp:tplink-smarthome:json:data-text-lines', 'eth:ethertype:ip:icmp:data', 'eth:ethertype:ip:udp:rdpudp:data', 'eth:ethertype:ip:icmp:ip', 'eth:ethertype:ip:udp:rx', 'eth:ethertype:ip:tcp:data', 'eth:ethertype:ip:udp:isakmp', 'eth:ethertype:ip:data', 'eth:ethertype:ip:tcp:tls:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509ce:x509ce:x509ce:x509ce:x509ce:x509ce:pkix1explicit:x509ce:pkix1implicit:x509ce:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509ce:x509ce:x509ce:x509ce:x509ce:x509ce:x509ce:pkix1implicit:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509ce:x509ce:x509ce:x509ce:x509ce:x509ce:pkix1implicit:tls', 'eth:ethertype:ip:icmp:ip:data', 'eth:ethertype:ip:udp:ssdp:data', 'eth:ethertype:ip:tcp:tls', 'eth:ethertype:ip:udp:goose:cotp:goose', 'eth:ethertype:ip:udp:classicstun:data', 'eth:ethertype:ip:tcp:tls:tls', 'eth:ethertype:ip:tcp', 'eth:ethertype:ip:udp:dns', 'eth:ethertype:ip:udp:snmp', 'eth:ethertype:ip:udp:classicstun', 'eth:ethertype:ip:icmp:ip:udp:ssdp', 'eth:ethertype:ip:icmp:ip:ipv6', 'eth:ethertype:ip:udp:rdpudp:dtls', 'eth:ethertype:ip:udp:rdpudp', 'eth:ethertype:ip:icmp:ip:udp:dns', 'eth:ethertype:ip:udp:ieee1722:data', 'eth:ethertype:ip:tcp:http', 'eth:ethertype:ip:udp:ntp', 'eth:ethertype:ip:udp:snmp:data', 'eth:ethertype:ip:udp:cldap']

zidian={}

for i in pro:
  zidian[i]=0

yingshe={'eth:ethertype:ip:data': 0, 'eth:ethertype:ip:icmp': 1, 'eth:ethertype:ip:icmp:data': 1, 'eth:ethertype:ip:icmp:ip': 1, 'eth:ethertype:ip:icmp:ip:data': 1, 'eth:ethertype:ip:icmp:ip:ipv6': 1, 'eth:ethertype:ip:icmp:ip:udp': 1, 'eth:ethertype:ip:icmp:ip:udp:classicstun': 1, 'eth:ethertype:ip:icmp:ip:udp:cldap': 1, 'eth:ethertype:ip:icmp:ip:udp:data': 1, 'eth:ethertype:ip:icmp:ip:udp:dns': 1, 'eth:ethertype:ip:icmp:ip:udp:ssdp': 1, 'eth:ethertype:ip:tcp': 2, 'eth:ethertype:ip:tcp:data': 2, 'eth:ethertype:ip:tcp:http': 3, 'eth:ethertype:ip:tcp:http:data-text-lines': 3, 'eth:ethertype:ip:tcp:tls': 4, 'eth:ethertype:ip:tcp:tls:tls': 4, 'eth:ethertype:ip:tcp:tls:x509sat:x509sat:x509ce': 4, 'eth:ethertype:ip:tcp:tls:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509ce:tls:x509ce:x509ce:pkix1implicit:x509ce:x509ce:pkix1explicit:x509ce:x509ce:x509ce:tls': 4, 'eth:ethertype:ip:tcp:tls:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509ce:x509ce:x509ce:x509ce:x509ce:x509ce:pkix1explicit:x509ce:pkix1implicit:x509ce:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509ce:x509ce:x509ce:x509ce:x509ce:x509ce:x509ce:pkix1implicit:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509ce:x509ce:x509ce:x509ce:x509ce:x509ce:pkix1implicit:tls': 4, 'eth:ethertype:ip:udp': 5, 'eth:ethertype:ip:udp:acdr': 5, 'eth:ethertype:ip:udp:bfd': 5, 'eth:ethertype:ip:udp:classicstun': 6, 'eth:ethertype:ip:udp:classicstun:data': 6, 'eth:ethertype:ip:udp:cldap': 7, 'eth:ethertype:ip:udp:data': 5, 'eth:ethertype:ip:udp:dns': 8, 'eth:ethertype:ip:udp:find': 5, 'eth:ethertype:ip:udp:goose:cotp:goose': 5, 'eth:ethertype:ip:udp:ieee1722:data': 5, 'eth:ethertype:ip:udp:isakmp': 9, 'eth:ethertype:ip:udp:memcache': 10, 'eth:ethertype:ip:udp:ntp': 11, 'eth:ethertype:ip:udp:rdpudp': 5, 'eth:ethertype:ip:udp:rdpudp:data': 5, 'eth:ethertype:ip:udp:rdpudp:dtls': 5, 'eth:ethertype:ip:udp:rip': 5, 'eth:ethertype:ip:udp:rx': 5, 'eth:ethertype:ip:udp:sip': 12, 'eth:ethertype:ip:udp:sip:sdp': 12, 'eth:ethertype:ip:udp:snmp': 13, 'eth:ethertype:ip:udp:snmp:data': 13, 'eth:ethertype:ip:udp:snmp:snmp': 13, 'eth:ethertype:ip:udp:snmp:snmp:snmp': 13, 'eth:ethertype:ip:udp:ssdp': 14, 'eth:ethertype:ip:udp:ssdp:data': 14, 'eth:ethertype:ip:udp:tplink-smarthome:json:data-text-lines': 5}
