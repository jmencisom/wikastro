# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib as url_op
import re
from BasicInfo import BasicInfo
from Image_NGC import Image_NGC
from datetime import date

def main():
	ngc = "NGC"
	ngc_num = askObjectNumber()
	webpage = ""

	ngc_num = str(ngc_num)
	ngc_nomb = ngc + " " + ngc_num
	print("\nobject: " + ngc_nomb)

	try:
		print("\nSearching object in database...\n")
		soup, webpage = obtainPage(ngc_num)
		text_basicInfo = getValues(soup)
		basicInfo = BasicInfo(text_basicInfo)
		image = Image_NGC(ngc_nomb)
		imageName = image.getImage()
		imageCaption = image.getCaption(ngc_nomb)


		coordinatesTextWiki = transformToCoordinatesWiki(
			basicInfo.getCoordinates())
		wikibox = transformToWikiBox(ngc_num, basicInfo, webpage, imageName,
			imageCaption)
		extraText = generateExtraInfo(ngc_num, webpage)

		print(wikibox)
		print(coordinatesTextWiki)
		print(extraText)
	except IOError as err:
		print ("\nCan not connect to Internet.\n")
	except IndexError as err:
		print("\nThe object was not found in database.\n")		



def generateExtraInfo(ngc_num, webpage):
	"""
	Generates external links section.
 
	Author: Andres Linares
	Date: 2018-02-14
	Modified: Never.
	Parameters: number of NGC object and url.
	Returns: String with external links for wikipedia.
	"""
	text = ("==External links==\n*[" + webpage + " NGC " + ngc_num + 
		" on SIMBAD" + "]\n")

	return text + "[[Category:NGC objects|" + ngc_num + "]]"



def getValues(soup):
	"""
	Using get_text() method from BeautifulSoup you get a lot of spaces
	and new line characters, then is required to get rid of them to
	ease the obtaining labor later.

	Author: Andres Linares.
	Date: 2018-02-14
	Modified: 2018-02-27 by Andres Linares.
	Parameters: BeautifulSoup object
	Returns: String that contains all the meaning data (basic info in simbad
	         database).
	"""
	childs = soup.get_text()
	text = ""
	flag = 0
	flag2 = 0

	for child in childs:
		if(child == "\n" and flag == 0):
			text = text + "\n"
			flag = 1
		if(child != " " and child != "\n"):
			flag = 0
			flag2 = 0
			text = text + child
		if(child == " " and flag == 0):
			text = text + " "
			flag2 = 1

	text = text.splitlines()
	text = text[len(text)-1]

	return text



def transformToWikiBox(ngc_num, basicInfo, webpage, imageName, imageCaption):
	
	"""
	This method creates a simple wikibox using the Infobox galaxy template.

	Author: Andres Linares.
	Date: 2018-02-14
	Modified: 2018-03-07 by Andres Linares
	Parameters: number of NGC object, basicInfo object, webpage, image
		file name and reference of the image file name.
	Returns: String to paste into wikipedia.
	"""
	reference = obtainReference(ngc_num, webpage)
	text = "{{Infobox galaxy\n"
	text = text + "| name = [[New General Catalogue|NGC]] " + ngc_num + "\n"
	text = text + "| image = " + imageName + "\n"
	text = text + "| caption = " + imageCaption + "\n"
	text = text + "| epoch = [[" + basicInfo.getEpoch() + "]]" + reference
	text = text + "| ra = {{RA|" + basicInfo.getCoordinates()[0] + "|" + basicInfo.getCoordinates()[1] + "|" + basicInfo.getCoordinates()[2] + "}} <ref name=\"simbad\" />\n"
	text = text + "| dec = {{DEC|" + basicInfo.getCoordinates()[3] + "|" +basicInfo.getCoordinates()[4] + "|" + basicInfo.getCoordinates()[5] + "}} <ref name=\"simbad\" />\n"
	text = text + "| constellation name = \n"
	text = (text + "| z = " + basicInfo.getRedShift() + " <ref name=\"simbad\" />\n") if (basicInfo.getRedShift() != "") else text + "| z = \n"																
	text = (text + "| h_radial_v = {{nowrap|" + basicInfo.getHelioRadialVelocity() + "[[Metre per second|km/s]]}} <ref name=\"simbad\" />\n") if (basicInfo.getHelioRadialVelocity() != "") else text + "| h_radial_v = \n" 
	text = text + "| gal_v = \n"																			
	text = text + "| dist_ly = \n"
	text = (text + "| type = " + basicInfo.getMorphologicalType() + "<ref name=\"simbad\" />\n") if (basicInfo.getMorphologicalType() != "") else text + "| type = \n"
	text = text + "| size_v = \n"
	text = text + "| appmag_b = " + basicInfo.getApparentMagnitude() + "<ref name=\"simbad\" />\n"
	text = text + "| notes = \n"
	text = text + "| names = " +basicInfo.getOtherNames() + " <ref name=\"simbad\" />\n"
	text = text + "}}"
	return text



def obtainReference(ngc_num, webpage):
	"""
	Elaborates a reference using the webpage of simbad, the number of the
	ngc object and today's date.

	Author: Andres Linares.
	Date: 2018-03-07
	Modified: Never.
	Parameters: Number of ngc object and url of the webpage.
	Returns: String with the reference.
	"""
	reference = ("<ref name=\"simbad\">{{cite web\n" +
	"  |title=SIMBAD Astronomical Database - CDS (Strasbourg)\n" +
	"  |work=Results for NGC " + ngc_num + "\n" + 
	"  |url=" + webpage + "\n" + 
	"  |accessdate=" + str(obtainActualDate()) + "}}</ref>\n")
	return reference



def obtainActualDate():
	"""
	Obtains actual date by using the datetime python library in the format
	yyyy-mm-dd

	Author: Andres Linares.
	Date: 2018-03-07
	Modified: Never.
	Parameters: Nothing
	Returns: Date object with today's date.
	"""
	today = date.today()
	return today


def transformToCoordinatesWiki(coordinates):
	"""
	Using the SKY_TEMPLATE found in wikipedia, the values are placed
 	just like the example.  Last value indicates the distance in light
 	years (not implemented yet).

	Author: Andres Linares.
	Date: 2018-02-13
	Modified: Never.
	Parameters: String array that contains right ascension in first three positions
		        and declination in last three.
	Returns: String to inject into wikipedia.
	"""
	text = "{{Sky|"
	for x in range(0, 6):
		text = text + coordinates[x]
		text = text + "|"
		if x == 2:
			text = text + "|"
	text = text + "999}}"
	return text



def askObjectNumber():
	"""
	Request an input that must be a positive number greater than zero.

	Author: Andres Linares.
	Date: 2018-02-13
	Modified: Never.
	Parameters: None.
	Returns: Integer greater than zero.
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




def obtainPage(ngc_num):
	"""
	Search a NGC object in simbad database and then returns the query in its
	full html page.  The search could be empty. This method uses urllib library.

	Author: Andres Linares.
	Date: 2018-02-13
	Modified: 2018-02-27 by Andres Linares
	Parameters: Integer encapsulated as a string.
	Returns: BeautifulSoup object encoded in 'lxml'
	"""
	searchingPt1 = ("http://simbad.u-strasbg.fr/simbad/sim-script?submit=" +
		"submit+script&script=format+object+form1+%22%25IDLIST%281%29" +
		"%7C%25COO%28%3BA%3BJ2000%29%7C%25COO%28%3BD%3BJ2000%29%7C+%25OTYPE" +
		"%28V%29%7C%25RV%28V%29%7C%25RV%28Z%29%7C%25FLUXLIST%28B%3B+F%29%7C" +
		"%25MT%28M%29%7C%25IDLIST%28SA%28%2c%20%29%3B%29%7C%22%0D%0A" +
		"query+id+ngc+")
	searchingPt2 = "%0D%0A"
	searchingWord = searchingPt1 + ngc_num + searchingPt2

	searchingURL1 = "http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=NGC+"
	searchingURL2 = "&submit=SIMBAD+search"
	searchingURLWord = searchingURL1 + ngc_num + searchingURL2
	webpage = searchingURLWord

	searchingPage = url_op.urlopen(searchingWord)
	return BeautifulSoup(searchingPage, "lxml"), webpage



if __name__ == "__main__":
	main()