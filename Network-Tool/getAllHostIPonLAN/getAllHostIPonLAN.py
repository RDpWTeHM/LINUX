#!/usr/bin/python3

"""=========================================================================
### <getAllHostIPonLAN.py>
### Copyright (C) <2018>  <Joseph Lin>
###
### This program is free software: you can redistribute it and/or modify
### it under the terms of the GNU General Public License as published by
### the Free Software Foundation, either version 3 of the License, or
### (at your option) any later version.
###
### This program is distributed in the hope that it will be useful,
### but WITHOUT ANY WARRANTY; without even the implied warranty of
### MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
### GNU General Public License for more details.
###
### You should have received a copy of the GNU General Public License
### along with this program.  If not, see <https://www.gnu.org/licenses/>.
###
###========================================================================"""

"""
#
# file name: getALlHostIPonLAN.py
# author   : Joseph Lin
# E-mail   : joseph.lin@aliyun.com
# function : N/A
#
###
### ------ 2018/Jun/28 20:35 ------
###  v0.0.1
### Author    : Joseph Lin
### function  : 简单将局域网端的所有 host 的 IP 输出（到 /tmp目录下的文件）。
### Change log: N/A
### Note      : 将 cat /proc/net/arp 放在 nmap 后面运行，会出比较怪异的结果！
###               在 terminal 中直接运行 nmap -sP <ip segement> 没有错误提示，
###             使用 os.system() 会有一行 udp 相关的错误提示！（虽然不影响输出结果）
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
	def __init__(self, nmapPath=None):
		if nmapPath == None:
			self.nmapPath = "/usr/local/bin/nmap"
		else:
			self.nmapPath = nmapPath
	#end func __init__.

	def getAllHostIPonLAN(self, segment, _stdout_flag):
		"""
		# segement: 192.168.1.0/24
		# usage: segement = "192.168.1.0/24"
		#        NetworkTool.getAllHostIPonLAN(segement)
		#
		"""
		## arp content!
		if _stdout_flag == "ON":
			os.system("cat /proc/net/arp")
		else:
			os.system("cat /proc/net/arp > /tmp/proc_net_arp.txt")

		if _stdout_flag == "ON":
			os.system("{} -sP {} ".format(self.nmapPath, segment))
		else:
			os.system("{} -sP {} > /tmp/nmap_-sP.txt 2>&1".format(self.nmapPath, segment))



#END class

###
### Tester
###
def main():
	argc = len(sys.argv)
	if argc != 2:
		print("Error command")
		print("usage: {} <ip segement>".format(sys.argv[0]))
		print("\tlike: {} 192.168.1.0/24".format(sys.argv[0]))
		sys.exit(1)

	## else, check ip segement Enter right!
	print("ip segement: {}".format(sys.argv[1]))

	networkTool = NetworkTool()
	segement = sys.argv[1]
	networkTool.getAllHostIPonLAN(segement)



if __name__ == '__main__':
	main()

