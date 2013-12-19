# -*- coding: utf-8 -*-
#
# get local IP, using my own service located at
# ip.malte-bublitz.de
#

from ip import *
from netifaces import interfaces, ifaddresses, AF_INET

def get_ip():
	ips = []
	for iface in interfaces():
		addresses = [i['addr'] for i in ifaddresses(iface).setdefault(AF_INET, [{'addr':None}] )]
		ips.append(addresses)
	return [IP(i[0]) for i in ips if i[0]]

if __name__=="__main__":
	all_ips = get_ip()
	for ip in all_ips:
		print(str(ip))
