#!/usr/bin/python3

"""
#
# file name: getALlHostIPonLAN.py
#
###
###
###
### -[o] cat /proc/net/arp run first, and analizy result.
###     namp run in another processing in the same time.
"""

###
### import packages 
###
import sys, os
import time

###
### global variables
###
doDebug = False


###
### function define.
###
class NetworkTool(object):
	def __init__(self):
		pass

	def getAllHostIPonLAN(self, segment):
		"""
		# segement: 192.168.1.0/24
		# usage: segement = "192.168.1.0/24"
		#        NetworkTool.getAllHostIPonLAN(segement)
		#
		"""
		os.system("/usr/local/bin/nmap -sP {} > /tmp/nmap_-sP.txt 2>&1".format(segment))
		#os.system("/usr/local/bin/nmap -sP {} ".format(segment))

		time.sleep(2)
		## arp content!
		os.system("cat /proc/net/arp > /tmp/proc_net_arp.txt")

#END class

###
### Tester
###
def main():
	networkTool = NetworkTool()
	segement = "192.168.29.0/24"
	networkTool.getAllHostIPonLAN(segement)



if __name__ == '__main__':
	main()

