# -*- coding: utf-8 -*-

import re
from BasicInfo import BasicInfo
from Image_NGC import Image_NGC
from WikiGeneration import WikiGeneration
from ObtainInfo import ObtainInfo

def main():
	"""
	This method asks for a number that means the number of a ngc object and
	and prints the text to paste into wikipedia as a new article.

	:Param: nothing.
	:Returns: nothing.
	"""
	ngc = "NGC"
	ngc_num = askObjectNumber()

	ngc_num = str(ngc_num)
	ngc_nomb = ngc + " " + ngc_num
	print("\nobject: " + ngc_nomb)

	webpage = ""
	try:
		print("\nSearching object in database...\n")
		obtainInfo = ObtainInfo()
		soup, webpage = obtainInfo.obtainPage(ngc_num)
		text_basicInfo = obtainInfo.getValues(soup)

		basicInfo = BasicInfo(text_basicInfo)
		
		image = Image_NGC(ngc_nomb)
		imageName = image.getImage()
		imageCaption = image.getCaption(ngc_nomb)

		wikiGeneration = WikiGeneration()
		coordinatesTextWiki = wikiGeneration.transformToCoordinatesWiki(
			basicInfo.getCoordinates())
		fatherPageTextWiki, objec = wikiGeneration.generateFatherPage(
			basicInfo.getObjectType())
		wikibox = wikiGeneration.transformToWikiBox(ngc_num, basicInfo, webpage,
		 	imageName, imageCaption)
		extraText = wikiGeneration.generateExtraInfo(ngc_num, webpage, objec)
		abstract = wikiGeneration.generateAbstract(ngc_num)
		observation = wikiGeneration.generateObservation()
		structure = wikiGeneration.generateStructure()

		print(coordinatesTextWiki)
		print(wikibox)
		print(abstract)
		print(observation)
		print(structure)
		print(fatherPageTextWiki)
		print(extraText)
	except IOError as err:
		print ("\nCan not connect to Internet.\n")
	except IndexError as err:
		print("\nThe object was not found in database.\n")		



def askObjectNumber():
	"""
	Request an input that must be a positive number greater than zero.

	
	:Param: None.
	:Returns: Integer greater than zero.
	:rtype: Integer
	"""
	while True:
		print("Type the number of the NGC object: ")
		try:
			ngc_num = int(input())
			if ngc_num > 0:
				return ngc_num
			else:
				print("Input must be positive and greater than zero.\n")
		except (ValueError, NameError, SyntaxError):
			print("Input must be a number.\n")