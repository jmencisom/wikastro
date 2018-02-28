from bs4 import BeautifulSoup
import urllib as url_op
import re

def main():
	ngc = "NGC"
	ngc_num = askObjectNumber()
	webpage = ""

	ngc_num = str(ngc_num)
	ngc_nomb = ngc + " " + ngc_num
	print("\nobject: " + ngc_nomb)
	print("\nsearching object in database...\n")

	soup, webpage = obtainPage(ngc_num)

	basicInfo = getValues(soup)
	basicInfoData = getOrganizatedData(basicInfo)
	
	coordinates = (basicInfoData[5] + " " + basicInfoData[7]).split()

	coordinatesTextWiki = transformToCoordinatesWiki(coordinates)
	wikibox = transformToWikiBox(ngc_num, basicInfoData[3], coordinates,
		basicInfoData[11], basicInfoData[9], basicInfoData[13],
		basicInfoData[15], webpage)
	extraText = generateExtraInfo(ngc_num, webpage)

	print(wikibox)
	print(coordinatesTextWiki)
	print(extraText)



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


	
def getOrganizatedData(basicInfoText):
	"""
	This method will try to obtain information such as:
	Object type (obj_typ)
	Epoch (epoch)
	Right Ascension Coordinates (coodRa)
	Declination Coordinates (coodD)
	Helio Radial Velocity (hrv)
	Red Shift (rs)
	Morphological type (morp_typ)
	Apparent magnitude B (b)

	Author: Andres Linares.
	Date: 2018-02-14
	Modified: 2018-02-27 by Andres Linares.
	Parameters: String that contains basic info about NGC object.
	Returns: String array.

	"""
	data = ["obj_typ", "",
			"epoch", "J2000",
			"coodRA", "",
			"coodD", "",
			"hrv", "",
			"rs", "",
			"morp_typ", "",
			"b", ""]
	basicInfoTextSeparated = basicInfoText.split("|")
	print(basicInfoTextSeparated)
	data[1] = basicInfoTextSeparated[3]
	data[5] = basicInfoTextSeparated[1]
	data[7] = basicInfoTextSeparated[2]
	data[9] = basicInfoTextSeparated[4]
	data[11] = basicInfoTextSeparated[5]
	data[13] = basicInfoTextSeparated[7]
	data[15] = basicInfoTextSeparated[6]

	return data



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



def transformToWikiBox(ngc_num, epoch, coordinates, redShift,
                       helioRadialVelocity, morphType, b, webpage):
	
	"""
	This method creates a simple wikibox using the Infobox galaxy template.

	Author: Andres Linares.
	Date: 2018-02-14
	Modified: Never.
	Parameters: number of NGC object, epoch, coordinates as an array, hrv,
	            morphtype, apparent magnitude b, url
	Returns: String to paste into wikipedia.
	"""
	text = "{{Infobox galaxy\n"
	text = text + "| name = [[New General Catalogue|NGC]] " + ngc_num + "\n"
	text = text + "| image = \n"
	text = text + "| caption = \n"
	text = text + "| epoch = [[" + epoch + "]]\n <ref name=\"simbad\">{{cite web|title=SIMBAD Astronomical" + "Database - CDS (Strasbourg)|work=Results for NGC " + ngc_num + "|url=" + webpage + "}}</ref>\n"
	text = text + "| ra = {{RA|" + coordinates[0] + "|" + coordinates[1] + "|" + coordinates[2] + "}} <ref name=\"simbad\" />\n"
	text = text + "| dec = {{DEC|" + coordinates[3] + "|" + coordinates[4] + "|" + coordinates[5] + "}} <ref name=\"simbad\" />\n"
	text = text + "| constellation name = \n"
	text = (text + "| z = " + redShift + " <ref name=\"simbad\" />\n") if (redShift != "") else text + "| z = \n"																
	text = (text + "| h_radial_v = {{nowrap|" + helioRadialVelocity + "[[Metre per second|km/s]]}} <ref name=\"simbad\" />\n") if (helioRadialVelocity != "") else text + "| h_radial_v = \n" 
	text = text + "| gal_v = \n"																			
	text = text + "| dist_ly = \n"
	text = (text + "| type = " + morphType + "<ref name=\"simbad\" />\n") if (morphType != "") else text + "| type = \n"
	text = text + "| size_v = \n"
	text = text + "| appmag_b = " + b + "<ref name=\"simbad\" />\n"
	text = text + "| notes = \n"
	text = text + "| names = \n"
	text = text + "}}"
	return text



"""
Author: Andres Linares.
Date: 2018-02-13
Modified: Never.
Parameters: String array that contains right ascension in first three positions
	        and declination in last three.
Returns: String to inject into wikipedia.
Description: Using the SKY_TEMPLATE found in wikipedia, the values are placed
	         just like the example.  Last value indicates the distance in light
             years (not implemented yet).
Example: {{Sky|00|07|15.86||27|42|29.7|190000000}}

"""
def transformToCoordinatesWiki(coordinates):
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
		print("type the number of the NGC object: ")
		try:
			ngc_num = int(input())
			if ngc_num > 0:
				return ngc_num
			else:
				print("input must be positive and greater than zero.\n")
		except ValueError:
			print("input must be a number.\n")




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
		"%28V%29%7C%25RV%28V%29%7C%25RV%28Z%29%7C%25FLUXLIST%28B%3B+F%29%7C%" + 
		"25MT%28M%29%7C%22%0D%0Aquery+id+ngc+")
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