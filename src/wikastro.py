# -*- coding: utf-8 -*-

import sys
import NGC
from clfs import clfs

def main(argv):
	"""
	Main method of the whole program. The objective of the parameters
	is to run certain script depending of which kind of object is
	desired to search.
	There are other options like for example: train the classifiers. In
	a future could be more.

	:Param: arguments.
	:Returns: nothing.
	"""
	if(len(argv) == 1):
		if(argv[0].upper() == "--NGC"):
			NGC.main()
		elif(argv[0].upper() == "--VERSION" or argv[0].upper() == "--V"):
			print("Wikastro v1.0")
		elif(argv[0].upper() == "--HELP" or argv[0].upper() == "--H"):
			print_help()
	elif(len(argv) == 2):
		if(argv[0].upper() == "--NGC" and argv[1].upper() == "--TRAIN"):
			clf = clfs()
			clf.train_ngc()
	else:
		print("Please use an option. For more information type --help")

def print_help():
	"""
	Prints the help of the script by command line.

	:Param: nothing.
	:Returns: nothing.
	"""
	print("""
Usage: python wikastro.py [option] [parameter]
Options:
--version: shows the version of the script.
--help: shows this message.
--ngc: runs NGC.py script.
-v: same as '--version'
-h: same as '--help'
Parameters:
--train: when '--ngc' is the option, you can type this parameter to train the classifier.
""")

if __name__ == "__main__":
	main(sys.argv[1:])