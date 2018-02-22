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

	try:
		soup = deleteFontTags(soup)
		basicInfoText = getMeaningValues(soup)
		basicInfoData = getOrganizatedData(basicInfoText)
		#print(basicInfoText)
		#print(basicInfoData)
		coordinatesTextWiki =  transformToCoordinatesWiki(basicInfoData[5].split())
		wikiBox = transformToWikiBox(ngc_num, basicInfoData[3],
									 basicInfoData[5].split(), basicInfoData[7],
									 basicInfoData[9], basicInfoData[11],
									 basicInfoData[13], webpage)

		extraText = generateExtraInfo(ngc_num, webpage)

		print(wikiBox)
		print(coordinatesTextWiki)
		print(extraText)
	except IndexError:
		print("\nObject not found in database...")



"""
Author: Andres Linares
Date: 2018-02-14
Modified: Never.
Parameters: number of NGC object and url.
Returns: String with external links for wikipedia.
Description: generates external links section.

"""
def generateExtraInfo(ngc_num, webpage):
	text = "==External links==\n*[" + webpage + " NGC " + ngc_num + " on SIMBAD" + "]\n"

	return text + "[[Category:NGC objects|" + ngc_num + "]]"

	
"""
Author: Andres Linares.
Date: 2018-02-14
Modified: Never.
Parameters: String that contains basic info about NGC object
Returns: String array.
Description: This method will try to obtain information such as:
	Object type (obj_typ): Galaxy (g)
	Epoch (epoch): J200...
	Coordinates (cood): xx xx xx.xxxx xx xx xx.xxxx
	Helio Radial Velocity (hrv): xxxx.xx
	Red Shift (rs): x.xxxxx
	Morphological type (morp_typ): Sabc...
	Apparent magnitude B (b): xx.xxx

"""
def getOrganizatedData(basicInfoText):
	data = ["obj_typ", "",
			"epoch", "",
			"cood", "",
			"hrv", "",
			"rs", "",
			"morp_typ", "",
			"b", ""]
	basicInfoTextSeparated = basicInfoText.splitlines()
	#data[1] = getObjectType(basicInfoTextSeparated)
	data[3] = getEpoch(basicInfoTextSeparated)
	data[5] = getCoordinates(basicInfoTextSeparated)
	data[7] = getHelioRadialVelocity(basicInfoTextSeparated)
	data[9] = getRedShift(basicInfoTextSeparated)
	data[11] = getMorphType(basicInfoTextSeparated)
	data[13] = getAM_B(basicInfoTextSeparated)

	return data


"""
Author: Andres Linares.
Date: 2018-02-14
Modified: Never.
Parameters: Text that contains basic info about NGC object and that is
            separated by lines.
Returns: String
Description: finds the apparent magnitud B.

"""
def getAM_B(basicInfoTextSeparated):
	flag = 0
	for text in basicInfoTextSeparated:
		if text.find("Fluxes") >= 0:
			flag = 1
		if text.find("B") == 0 and flag == 1:
			return text.split()[1]
	return ""



"""
Author: Andres Linares.
Date: 2018-02-14
Modified: Never.
Parameters: Text that contains basic info about NGC object and that is
            separated by lines.
Returns: String.
Description: finds the morphological type.

"""
def getMorphType(basicInfoTextSeparated):
	flag = 0
	for text in basicInfoTextSeparated:
		if flag == 1:
			return text
		if text.find("Morphological") >= 0:
			flag = 1
	return ""



"""
Author: Andres Linares.
Date: 2018-02-14
Modified: Never.
Parameters: Text that contains basic info about NGC object and that is
            separated by lines.
Returns: String.
Description: finds the epoch.

"""
def getEpoch(basicInfoTextSeparated):
	for text in basicInfoTextSeparated:
		if text.find("ep=") >= 0:
			startPosition = text.find("=")
			finalPosition = text.find(")")
			return text[startPosition+1:finalPosition]
	return ""


	
"""
Author: Andres Linares.
Date: 2018-02-14
Modified: Never.
Parameters: BeautifulSoup object
Returns: String that contains all the meaning data (basic info in simbad
         database).
Description: Using get_text() method from BeautifulSoup you get a lot of spaces
             and new line characters, then is required to get rid of them to
             ease the obtaining labor later.  The string ends when it finds a
             'SIMBAD' word in it.

"""
def getMeaningValues(soup):
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
		if(text.find("SIMBAD") > 0):
			break

	return text


"""
Author: Andres Linares
Date: 2018-02-14
Modified: Never.
Parameters: BeautifulSoup object.
Returns: BeautifulSoup object without <font size="-1"> </font>tags.
Description: removes every single font tag with size -1 in the object passed
             by parameter.

"""
def deleteFontTags(soup):
	soup = soup.body.find_all("table")[2]
	fontMinusOne = soup.find_all("font", size="-1")

	for font in fontMinusOne:
		font.decompose()
	return soup



"""
Author: Andres Linares.
Date: 2018-02-14
Modified: Never.
Parameters: number of NGC object, epoch, coordinates as an array, hrv,
            morphtype, apparent magnitude b, url
Returns: String to paste into wikipedia.
Description: This method creates a simple wikibox using the Infobox galaxy
             template.

"""
def transformToWikiBox(ngc_num, epoch, coordinates, redShift,
                       helioRadialVelocity, morphType, b, webpage):
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



"""
Author: Andres Linares.
Date: 2018-02-14
Modified: Never.
Parameters: Text that contains basic info about NGC object and that is
            separated by lines.
Returns: String.
Description: finds the red shift.

"""
def getRedShift(basicInfoTextSeparated):
	flag = 0
	for text in basicInfoTextSeparated:
		if flag == 1:
			return text.split()[1]
		if text.find("km/s") >= 0:
			flag = 1
	return ""



"""
Author: Andres Linares.
Date: 2018-02-14
Modified: Never.
Parameters: Text that contains basic info about NGC object and that is
            separated by lines.
Returns: String.
Description: finds the helio radial velocity.

"""
def getHelioRadialVelocity(basicInfoTextSeparated):
	flag = 0
	for text in basicInfoTextSeparated:
		if flag == 1:
			return text.split()[1]
		if text.find("Radial velocity") >= 0:
			flag = 1
	return ""



"""
Author: Andres Linares.
Date: 2018-02-14
Modified: Never.
Parameters: Text that contains basic info about NGC object and that is
            separated by lines.
Returns: String.
Description: finds the coordinates.

"""
def getCoordinates(basicInfoTextSeparated) :
	flag = 0
	for text in basicInfoTextSeparated:
		if flag == 1:
			return text
		if text.find("ep=") > 0:
			flag = 1
	return ""



"""
Author: Andres Linares.
Date: 2018-02-13
Modified: Never.
Parameters: None.
Returns: Integer greater than zero.
Description: Request an input that must be a positive number greater than zero.

"""
def askObjectNumber():
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



"""
Author: Andres Linares.
Date: 2018-02-13
Modified: Never.
Parameters: Integer encapsulated as a string.
Returns: BeautifulSoup object encoded in 'lxml'
Description: Search a NGC object in simbad database and then returns the
	         query in its full html page.  The search could be empty.
             This method uses urllib.request library.

"""
def obtainPage(ngc_num):
	searchingPt1 = "http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=NGC+"
	searchingPt2 = "&submit=SIMBAD+search"
	searchingWord = searchingPt1 + ngc_num + searchingPt2
	webpage = searchingWord

	searchingPage = url_op.urlopen(searchingWord)
	return BeautifulSoup(searchingPage, "lxml"), webpage



if __name__ == "__main__":
	main()