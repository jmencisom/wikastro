# -*- coding: utf-8 -*-

import sys
import NGC

def main(argv):
	if(len(argv) == 1):
		if(argv[0].upper() == "--NGC"):
			NGC.main()
		elif(argv[0].upper() == "--VERSION" or argv[0].upper() == "--V"):
			print("Wikastro v1.0")
		elif(argv[0].upper() == "--HELP" or argv[0].upper() == "--H"):
			print_help()
	else:
		print("Please use an option. For more information type --help")

def print_help():
	print("""
Usage: python wikastro.py [option]
Options:
--version: shows the version of the script.
--help: shows this message.
--ngc: runs NGC.py script.
-v: same as '--version'
-h: same as '--help'
		""")

if __name__ == "__main__":
	main(sys.argv[1:])