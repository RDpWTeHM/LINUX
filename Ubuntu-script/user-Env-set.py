#!/usr/bin/python3

"""
# file name: user-Env-set.py
# Author   : Joseph Lin
# E-mail   : joseph.lin@aliyun.com
#
###
###
###  
"""


###
### import packages
###
import os, sys

import getpass ## get system login username.

###
### global variables
###
doDebug = False

###
### function defines
###
def foo():
	pass

###
### running logical:
###
def main():
	PS1 = "PS1=\"\\[\\e]0;\\u@\\h: \\w\\a\\]${debian_chroot:+($debian_chroot)}\\[\\033[01;32m\\]\\u@\\h\\[\\033[00m\\]:\\[\\033[01;34m\\]\\W\\[\\033[00m\\]\\$ \""
	### get "USER" name of LINUX.
	LINUX_userName = getpass.getuser()
	bashrcPath = "/home/%s/.bashrc" %LINUX_userName

	try:
		with open(bashrcPath, 'a') as bashrcfp:
			print("", file=bashrcfp)
			print("%s" %PS1, file=bashrcfp)
			print("export PS1", file=bashrcfp)
			print("\n", file=bashrcfp)
	except:
		print("bashrc file oprate error!", sys.stderr)

#END main.

if __name__=="__main__":
	main()

#END

