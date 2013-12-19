# -*- coding: utf-8 -*-
#
# basic class for storing an IP address
#

class IP(object):
	ip = None
	def __init__(self, ip=None):
		self.ip = ip
	def setIP(self, ip):
		self.ip = ip
	def getIP(self):
		return self.ip
	def __repr__(self):
		return '<IP '+self.ip+'>'
	def __str__(self):
		return self.ip

