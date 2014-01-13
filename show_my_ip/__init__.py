# -*- coding: utf-8 -*-

from ip import IP
from get_global import get_ip as get_global_ip
from get_local import get_ip as get_local_ip

if __name__=='__main__':
	import sys
	if len(sys.argv)>=2 and not sys.argv[1] in ("--help", "--version", "-h", "-V"):
		if sys.argv[1]=="global":
			print("Global IP:")
			_global = get_global_ip()
			print(str(_global))
		elif sys.argv[1]=="local":
			print("Local IP(s):")
			_local = get_local_ip()
			for ip in _local:
				print(str(ip))
		elif sys.argv[1]=="test":
			if len(sys.argv)==3:
				print(str(IP(sys.argv[2])))
			else:
				print(str(IP("178.63.11.250")))
		else:
			print "Unknown command."
	else:
		print("Local IP(s):")
		_local = get_local_ip()
		for ip in _local:
			print(str(ip))
		print("Global IP:")
		_global = get_global_ip()
		print(str(_global))

