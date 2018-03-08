# -*- coding: utf-8 -*-

from datetime import date

class WikiGeneration:



	def __init__(self):
		pass



	def generateExtraInfo(self, webpage, ngc_num):
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



	def __obtainReference(self, ngc_num, webpage):
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
		"  |accessdate=" + str(self.__obtainActualDate()) + "}}</ref>\n")
		return reference



	def __obtainActualDate(self):
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



	def transformToCoordinatesWiki(self, coordinates):
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



	def transformToWikiBox(self, ngc_num, basicInfo, webpage, imageName,
		imageCaption):
		"""
		This method creates a simple wikibox using the Infobox galaxy template.

		Author: Andres Linares.
		Date: 2018-02-14
		Modified: 2018-03-07 by Andres Linares
		Parameters: number of NGC object, basicInfo object, webpage, image
			file name and reference of the image file name.
		Returns: String to paste into wikipedia.
		"""
		reference = self.__obtainReference(ngc_num, webpage)
		ref = "<ref name=\"simbad\" />\n"
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
		text = text + "| appmag_b = " + basicInfo.getApparentMagnitude() + ref
		text = text + "| notes = \n"
		text = text + "| names = " + basicInfo.getOtherNames() + ref
		text = text + "}}"
		return text