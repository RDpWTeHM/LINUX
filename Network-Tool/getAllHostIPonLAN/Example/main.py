#!/usr/bin/python3

"""=========================================================================
### <main.py   Tester of getAllHostIPonLAN.py>
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
# file name: main.py
# function : modules Tester
# author   : Jospeh Lin
# E-mail   : joseph.lin@aliyun.com 
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


import getAllHostIPonLAN
###
### global variables
###
doDebug = False



###
### function define.
###


###
### Tester
###
def main():
	argc = len(sys.argv)
	if argc < 2:
		print("Error command")
		print("usage: {} <ip segement>".format(sys.argv[0]))
		print("\tlike: {} 192.168.1.0/24".format(sys.argv[0]))
		sys.exit(1)

	## else, check ip segement Enter right!
	print("ip segement: {}".format(sys.argv[1]))

	## STDOUT_flag = 'OFF/ON'
	if argc == 3:
		STDOUT_flag = sys.argv[2]

	networkTool = getAllHostIPonLAN.NetworkTool()
	segement = sys.argv[1]
	networkTool.getAllHostIPonLAN(segement, STDOUT_flag)



if __name__ == '__main__':
	main()

