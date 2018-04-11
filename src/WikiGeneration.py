# -*- coding: utf-8 -*-

from datetime import date

class WikiGeneration:



	def __init__(self):
		"""
		There is no need to initialize the class with any variables.
		"""
		pass



	def generateExtraInfo(self, ngc_num, webpage):
		"""
		Generates external links section.
	 
		Author: Andres Linares
		Date: 2018-02-14
		Modified: 2018-03-08 by Andres Linares.
		Parameters: number of NGC object and url.
		Returns: String with external links for wikipedia.
		"""
		text = ("==External links==\n*[{0} NGC {num} on SIMBAD]\n" +
			"[[Category:NGC objects|{num}]]").format(webpage, num = ngc_num)
		return text



	def __obtainReference(self, ngc_num, webpage):
		"""
		Elaborates a reference using the webpage of simbad, the number of the
		ngc object and today's date.

		Author: Andres Linares.
		Date: 2018-03-07
		Modified: 2018-03-08 by Andres Linares.
		Parameters: Number of ngc object and url of the webpage.
		Returns: String with the reference.
		"""
		reference = ("<ref name=\"simbad\">{{{{cite web\n" +
		"  |title=SIMBAD Astronomical Database - CDS (Strasbourg)\n" +
		"  |work=Results for NGC {0}\n" + 
		"  |url={1}\n" + 
		"  |accessdate={2}}}}}</ref>").format(ngc_num, webpage,
				str(self.__obtainActualDate()))
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
		Modified: 2018-04-10 by Lina Mejia
		Parameters: number of NGC object, basicInfo object, webpage, image
			file name and reference of the image file name.
		Returns: String to paste into wikipedia.
		"""
		reference = self.__obtainReference(ngc_num, webpage)
		ref = "<ref name=\"simbad\" />"

		text = ("{{{{Infobox galaxy\n"
			"| name = [[New General Catalogue|NGC]] {num}\n"
			"| image = {image}\n"
			"| caption = {caption}\n"
			"| epoch = [[{epoch}]]{reference}\n"
			"| ra = {{{{RA{coorRA}}}}}{ref}\n"
			"| dec = {{{{DEC{coorDEC}}}}}{ref}\n"
			"| constellation name = {const_name}\n"
			"| z = {z}{ref}\n"
			"| h_radial_v = {{{{nowrap|{hrv}[[Metre per second|km/s]]}}}}{ref}\n"
			"| type = {type}{ref}\n"
			"| appmag_b = {b}{ref}\n"
			"| dist_ly = {distance} [light-year|ly]\n"
			"| names = {names}{ref}\n"
			"}}}}").format(num = ngc_num, image = imageName,
				caption = imageCaption, epoch = basicInfo.getEpoch(),
				reference = reference, ref = ref,
				coorRA = self.__transformCoordinatesRA(basicInfo.getCoordinates()),
				coorDEC = self.__transformCoordinatesDEC(basicInfo.getCoordinates()),
				const_name = basicInfo.getConstellation(),
				z = basicInfo.getRedShift(),
				hrv = basicInfo.getHelioRadialVelocity(),
				type = basicInfo.getMorphologicalType(),
				b = basicInfo.getApparentMagnitude(),
				distance = basicInfo.getDistance(),
				names = basicInfo.getOtherNames())
		return text



	def __transformCoordinatesRA(self, coordinates):
		"""
		This method receives the coordinates as a list, and the first
		three positions of this list corresponds to the right ascension.

		parameters: coordinates as a list.
		returns: string in the format {}|{}|{}
		"""
		text = "|{0}|{1}|{2}".format(coordinates[0], coordinates[1],
			coordinates[2])
		return text



	def __transformCoordinatesDEC(self, coordinates):
		"""
		This method receives the coordinates as a list, and the
		last three positions of this list corresponds to the declination.

		parameters: coordinates as a list.
		returns: string in the format |{}|{}|{}
		"""
		text = "|{0}|{1}|{2}".format(coordinates[3], coordinates[4],
			coordinates[5])
		return text