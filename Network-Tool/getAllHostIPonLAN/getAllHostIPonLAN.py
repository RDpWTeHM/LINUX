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
### ------ 2018/Jun/28 22:54 ------
###  v0.0.2
### Author    : Joseph Lin
### Change Log:   更新了 getAllHostIPonLAN() 函数代码， 将v0.0.1 的简单输出
###             通过 re 正则表达库 分析出 IP 地址， 然后返回list给调用。
### Note      : 了解一下 code， 简单可以知道，command 的 ON/OFF 作用的位置发生变化。 
###
### ------
###  -[o] cat /proc/net/arp run first, and analizy result.
###      namp run in another processing in the same time.
###      虚拟机测试 需要 15s+ 运行完 nmap -sP.
###
"""

###
### import packages 
###
import sys, os
import time

import re  ## default. 


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

	def getAllHostIPonLAN(self, segment, _stdout_flag="OFF"):
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

		reRuleofIP = r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"

		result1 = None
		try:
			with open("/tmp/proc_net_arp.txt") as fp1: 
				data1 = fp1.read()
				result1 = re.findall(reRuleofIP, data1)
		except:
			pass

		result2 = None
		try:
			with open("/tmp/nmap_-sP.txt") as fp2:
				data2 = fp2.read()
				result2 = re.findall(reRuleofIP, data2)
		except:
			pass

		allIPAddr = list()
		if result1 != None:
			if result1:
				for eachIP in result1:
					allIPAddr.append(eachIP)
		if result2 != None:
			if result2:
				for eachIP in result2:
					allIPAddr.append(eachIP)

		allIPAddrSET = set(allIPAddr)
		allIPAddr = list(allIPAddrSET)

		return allIPAddr
#END class

###
### Tester
###
def main():
	argc = len(sys.argv)
	if argc < 3:
		print("Error command")
		print("usage: {} <ip segement> <STDOUT flag>".format(sys.argv[0]))
		print("\tlike: {} 192.168.1.0/24 ON(or OFF)".format(sys.argv[0]))
		sys.exit(1)

	## else, check ip segement Enter right!
	print("ip segement: {}".format(sys.argv[1]))

	networkTool = NetworkTool()
	segement = sys.argv[1]
	allIPAddr = networkTool.getAllHostIPonLAN(segement)


	if sys.argv[2] == "ON":
		print(allIPAddr)
	else:
		try: 
			with open("/tmp/allLANHostIP.txt", "w") as fp:
				for eachIP in allIPAddr:
					print("{}".format(eachIP), file=fp)
		except:
			print("something wrong when print out Result!", file=sys.stderr)

if __name__ == '__main__':
	main()

