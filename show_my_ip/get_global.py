# -*- coding: utf-8 -*-
#
# get global IP, using my own service located at
# ip.malte-bublitz.de
#

from ip import *
import socket

def get_ip():
	s = socket.socket(
			socket.AF_INET,
			socket.SOCK_STREAM
			)
	s.connect(
			(
				"ip.malte-bublitz.de",
				79
			)
		)
	s.send("ip\r\n")
	ip = s.recv(1024).strip()
	return IP(ip)

if __name__=="__main__":
	print(str(get_ip()))
