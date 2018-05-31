# -*- coding: utf-8 -*-

from datetime import date

class WikiGeneration:



	def __init__(self):
		"""
		There is no need to initialize the class with any variables.
		"""
		pass



	def generateExtraInfo(self, ngc_num, webpage, objec):
		"""
		Generates external links section.
	 
		
		:Param: number of NGC object and url.
		:Returns: String with external links for wikipedia.
		:rtype: String 
		"""
		x=int(int(ngc_num)-1)/500
		x=(x+1)*5;
		if objec != "Galaxy":
			objec = ""
		text = ("==External links==\n*[{0} NGC {num} on SIMBAD]\n\n==References"
				+"==\n{{{{reflist}}}}\n[[Category:NGC objects|{num}]]\n"
				+"\n{{{{commonscat}}}}\n{{{{{Type}}}}}\n{{{{Ngc{x}}}}}"
				).format(webpage, num = ngc_num,Type = objec, x=x)
		
		

		return text

	def generateFatherPage(self, objectType):
		"""
		It generates to see also the section, from the relation 
		of simbad objects and wikipedia
	 
		
		:Param: objectType.
		:Returns: String with see also.
		:rtype: String 
		"""
		objectt=[[" Association of Stars","Star"],
				[" Herbig Ae/Be Star","Nebula"],
				[" Star Forming Region","Nebula"],
				[" Emission Object","Nebula"],
				[" Cluster of Stars","Open Cluster"],
				[" Double or Multiple Star","Star"],
				[" Reflection Nebula","Nebula"],
				[" Liner-Type Active Galaxy Nucleus","Galaxy"],
				[" Seyfert 2 Galaxy","Galaxy"],
				[" Galaxy in Cluster of Galaxies","Galaxy"],
				[" Galaxy","Galaxy"],
				[" Brightest Galaxy in A Cluster (Bcg)","Galaxy"],
				[" Open (Galactic) Cluster","Open Cluster"],
				[" Globular Cluster","Globular Cluster"],
				[" Herbig-Haro Object","Nebula"],
				[" Interacting Galaxies","Galaxy"],
				[" Galaxy in Pair of Galaxies","Galaxy"],
				[" Hii Galaxy","Galaxy"],
				[" Radio Galaxy","Galaxy"],
				[" Low Surface Brightness Galaxy","Galaxy"],
				[" Pair of Galaxies","Galaxy"],
				[" Hii (Ionized) Region","Nebula"],
				[" Bright Nebula","Nebula"],
				[" Blazar","Galaxy"],
				[" Blue Compact Galaxy","Galaxy"],
				[" Emission-Line Star","Star"],
				[" Galactic Nebula","Nebula"],
				[" Galaxy in Group of Galaxies","Galaxy"],
				[" Group of Galaxies","Galaxy Cluster"],
				[" Molecular Cloud","Nebulosa"],
				[" Moving Group","Open Cluster"],
				[" Nova","Star"],
				[" Part of A Galaxy","Galaxy"],
				[" Possible (Open) Star Cluster","Star"],
				[" Possible Quasar","Galaxy"],
				[" Spectroscopic Binary","Star"],
				[" Variable Star of Orion Type","Star"],
				[" Interstellar Matter","Nebula"],
				[" Object of Unknown Nature","Open Cluster"],
				[" Planetary Nebula","Nebula"],
				[" Seyfert Galaxy","Galaxy"],
				[" Seyfert 1 Galaxy","Galaxy"],
				[" Emission-Line Galaxy","Galaxy"],
				[" Active Galaxy Nucleus","Galaxy"],
				[" Starburst Galaxy","Galaxy"],
				[" Quasar","Galaxy"],
				[" Star","Star"],
				[" Supernova Remnant"," Nebula"]]

		x=0	
		while x < 48 :
			if objectt[x][0] == objectType:
				text = objectt[x][1]
				x=48
			if x == 47 :
				text = ""
			x += 1
		objec = text
		text = ("\n==See also==\n*[[{text}]]\n").format(text = text )

		return text, objec


	def generateAbstract(self, ngc_num):
		text = "\n'''NGC {}''' is a \n".format(ngc_num)
		return text


	def generateObservation(self):
		text = "\n== Observation ==\n"
		return text


	def generateStructure(self):
		text = "\n== Structure ==\n"
		return text


	def __obtainReference(self, ngc_num, webpage):
		"""
		Elaborates a reference using the webpage of simbad, the number of the
		ngc object and today's date.

		
		:Param: Number of ngc object and url of the webpage.
		:Returns: String with the reference.
		:rtype: String 
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

		
		:Param: Nothing
		:Returns: Date object with today's date.
		:rtype: Date
		"""
		today = date.today()
		return today



	def transformToCoordinatesWiki(self, coordinates):
		"""
		Using the SKY_TEMPLATE found in wikipedia, the values are placed
	 	just like the example.  Last value indicates the distance in light
	 	years (not implemented yet).

		
		:Param: String array that contains right ascension in first three positions
			        and declination in last three.
		:Returns: String to inject into wikipedia.
		"""

		text = "{{Sky|"
		for x in range(0, 6):
			text = text + coordinates[x]
			text = text + "|"
			if x == 2:
				text = text + "|"
		text = text + "999}}\n"
		return text



	def transformToWikiBox(self, ngc_num, basicInfo, webpage, imageName,
		imageCaption):
		"""
		This method creates a simple wikibox using the Infobox galaxy template.

		
		:Param: number of NGC object, basicInfo object, webpage, image
			file name and reference of the image file name.
		:Returns: String to paste into wikipedia.
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
			"| dist_ly = {distance}[light-year|ly]\n"
			"| discoverer = {discovery[0]}\n"
			"| year of discovery = {discovery[1]}\n"			
			"| names = {names}{ref}"
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
				discovery = basicInfo.getDiscovererAndYear(ngc_num),
				names = basicInfo.getOtherNames())
		return text



	def __transformCoordinatesRA(self, coordinates):
		"""
		This method receives the coordinates as a list, and the first
		three positions of this list corresponds to the right ascension.

		:Param: coordinates as a list.
		:Returns: string in the format {}|{}|{}
		"""
		text = "|{0}|{1}|{2}".format(coordinates[0], coordinates[1],
			coordinates[2])
		return text



	def __transformCoordinatesDEC(self, coordinates):
		"""
		This method receives the coordinates as a list, and the
		last three positions of this list corresponds to the declination.

		:Param: coordinates as a list.
		:Returns: string in the format |{}|{}|{}
		"""
		text = "|{0}|{1}|{2}".format(coordinates[3], coordinates[4],
			coordinates[5])
		return text