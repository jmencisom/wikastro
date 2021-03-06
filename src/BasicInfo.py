# -*- coding: utf-8 -*-

import os
import urllib as url_op
from astropy.coordinates import SkyCoord, get_constellation
from astropy import units as u
from astropy.cosmology import WMAP9 as cosmo
from astropy.coordinates import Distance

class BasicInfo:

	def __init__(self, attributes):
		"""
		Receives the attributes in a string and then assigns these values into
		the class variables.

		
		:Param: String that contains basic info separated by '|'
		:Return: Nothing.
		"""
		self.__attributes = attributes
		self.__objectType = ""
		self.__nombre=""
		self.__epoch = "J2000"
		self.__rightAscension = ""
		self.__declination = ""
		self.__helioRadialVelocity = ""
		self.__redShift = ""
		self.__morphologicalType = ""
		self.__apparentMagnitude = ""
		self.__otherNames = ""

		self.__namesReferences = [[" UGC", " [[Uppsala General Catalogue|UGC]]"],
			[" PGC", " [[Principal Galaxies Catalogue|PGC]]"],
			[" MCG", " [[Morphological Catalogue of Galaxies|MCG]]"],
			[" GC", " [[Catalogue of Nebulae and Clusters of Stars|GC]]"],
			[" CGCG", " [[Catalogue of Galaxies and Clusters of Galaxies|CGCG]]"],
			[" NGC", " [[New General Catalogue|NGC]]"],
			[" ESO", " [[ESO]]"],
			[" Tuc", " [[Bayer designation|&xi; Tuc]]"],
			[" 1RXS", " [[1RXS]]"],
			[" 2MASX", " [[2MASX]]"]]
		self.__obtainValues()



	def __obtainValues(self):
		"""
		Using the variable 'self.__attributes', a string array is obtained
		and then each individual string is assigned to differents
		clas variables.

		
		:Param: Nothing.
		:Returns: Nothing.
		"""
		separatedText = self.__attributes.split("|")
		self.__nombre = separatedText[0]
		self.__objectType = separatedText[3]
		self.__rightAscension = separatedText[1]
		self.__declination = separatedText[2]
		self.__helioRadialVelocity = separatedText[4]
		self.__redShift = separatedText[5]
		self.__morphologicalType = separatedText[7]
		self.__apparentMagnitude = separatedText[6]
		self.__otherNames = self.formatOtherNames(separatedText[8])



	def setAttributes(self, attributes):
		"""
		Assign the attributes received in the parameters into the
		attributes from the class and then calls the method obtainValues()
		in order to get a better organization.

		:Param: attributes obtained from the simbad database.
		:Returns: nothing.
		"""
		self.__attributes = attributes
		self.__obtainValues()



	def getAttributes(self):
		"""
		Obtain the attributes from the class and returns it.
		The variable attributes is the text recieved from the simbad
		database.

		:Param: nothing.
		:Returns: attributes from the class.
		"""
		return self.__attributes



	def getObjectType(self):
		"""
		If the object type is not empty, returns its containt. Else, it returns
		a string that contains just a emptiness.

		:Param: nothing.
		:Returns: object type.
		"""
		if(self.testEmptiness(self.__objectType, "Object Type")):
			return ""
		else:
			return self.__objectType



	def getEpoch(self):
		"""
		Returns the epoch of the NGC object, this variable usually contains
		J2000 epoch.

		:Param: nothing.
		:Returns: epoch.
		"""
		return self.__epoch



	def getRightAscension(self):
		"""
		Returns the right ascension inside the coordinates of the ngc object.
		If the variable is empty, then is return an empty string.

		:Param: nothing.
		:Returns: right ascension.
		"""
		if(self.testEmptiness(self.__rightAscension, "Right Ascension")):
			return ""
		else:
			return self.__rightAscension



	def getDeclination(self):
		"""
		Returns the declination inside the coordinates of the ngc object.
		If the variable is empty, then is return an empty string.

		:Param: nothing.
		:Returns: declination.
		"""
		if(self.testEmptiness(self.__declination, "Declination")):
			return ""
		else:
			return self.__declination



	def getHelioRadialVelocity(self):
		"""
		Returns the helio radial velocity also known as hrv of the ngc object.
		If the variable is empty, then is return an empty string.

		:Param: nothing.
		:Returns: helio radial velocity.
		"""
		if(self.testEmptiness(self.__helioRadialVelocity,
				"Helio Radial Velocity")):
			return ""
		else:
			return self.__helioRadialVelocity



	def getRedShift(self):
		"""
		Returns the red shift also known as z of the ngc object.
		If the variable is empty, then is return an empty string.

		:Param: nothing.
		:Returns: red shift.
		"""
		if(self.testEmptiness(self.__redShift, "Red Shift")):
			return ""
		else:
			return self.__redShift



	def getMorphologicalType(self):
		"""
		Returns the morphological type of the ngc object that is usually
		abreviated by the simbad database as some casual objects like
		galaxies, stars, etc.

		:Param: nothing.
		:Returns: morphological type.
		"""
		if(self.testEmptiness(self.__morphologicalType, "Morphological Type")):
			return ""
		else:
			return self.__morphologicalType



	def getApparentMagnitude(self):
		"""
		Returns the apparent magnitude also known as B of the ngc object.
		If the variable is empty, then is return an empty string.

		:Param: nothing.
		:Returns: morphological type.
		"""
		if(self.testEmptiness(self.__apparentMagnitude, "Apparent Magnitude")):
			return ""
		else:
			return self.__apparentMagnitude



	def getOtherNames(self):
		"""
		Returns the other names of an ngc object. this variable could contain
		a lot of different not so known names or could be just one single name.

		:Param: nothing.
		:Returns: other names of the ngc object as a string.
		:rtype: String
		"""
		if(self.testEmptiness(self.__otherNames, "Other Names")):
			return ""
		else:
			return self.__otherNames



	def getCoordinates(self):
		"""
		This method concatenates the right ascension and the declination
		into a single string.

		
		:Param: Nothing.
		:Returns: Coordinates in the form: right_ascension declination.
		"""
		return (self.getRightAscension() + " " + self.getDeclination()).split()



	def getConstellation(self):
		"""
		Coming soon...

		"""
		ra=self.getRightAscension()
		dec=self.getDeclination()
		ra2=ra.split(" ")
		dec2=dec.split(" ")
		ra=ra2[0]+"h"+ra2[1]+"m"+ra2[2]+"s"
		dec=dec2[0]+"d"+dec2[1]+"m"+dec2[2]+"s"
		constellation = SkyCoord(ra, dec, frame='icrs')
		return get_constellation(constellation)



	def getDistance(self):
		"""
		This method returns the distance of the object.

		
		:Param: Nothing.
		:Returns: Float with the distance of the object in lightyears units.
		:rtype: Float
		"""

		
		if (self.getRedShift() != ""):
			r = float(self.getRedShift())
			d2 = Distance(cosmo.comoving_distance(r), u.lightyear)
			value = float(str(d2).split()[0])
			divided = value / 1000000 #1 million
			if divided > 1:
				return "{:.2f} M".format(divided)
			else:
				return "{:.2f} ".format(value)
		else:
			return ""



	def getDiscovererAndYear(self,ngc_num):
		"""
 		This method returns the discoverer of the object and the
        year it was discovered.

        
        :Param: the number of the object required.
        :Returns: String array of two positions that contains the discoverer and
         the year respectively.
		:rtype: String
		"""
		discoverer=""
		year=""
		try:
			if(os.path.exists('info.txt')):
				pass
			else:
				page = 'http://ngcicproject.org/public_HCNGC/DPublic_HCNGC.txt'
				url_op.urlretrieve(page, "info.txt")


			self.ngc_num = int(ngc_num)+9
			archivo = open("info.txt")
			cont=0

			while  cont != self.ngc_num:
					linea=archivo.readline()	
					cont+=1

			arr = linea.split("|")
			discoverer = arr[9]
			year = arr[10]
		except:
			print "Error found"
		return [discoverer, year]


	def formatOtherNames(self, names):
		"""
		This method checks that the main name is not included and also 
		adds the known references.

		
		:Param: A string that contains the list of names returned by simbad.
		:type: String 
		:Returns: A String that contains the referenced names.
		:rtype: String 
		"""
		format_names=names[names.find(",")+1:] #elimina primer nombre (NGC)
		for ref in self.__namesReferences:
			format_names=format_names.replace(ref[0], ref[1])
		return format_names



	def testEmptiness(self, variable, name):
		"""
		This method test the emptiness of a variable. The emptiness is
		represented by a empty string '' or by this string: '~'. If
		the variable is empty then True is returned.

		
		:Param: Variable to test and name of the variable to print.
		:Returns: True if variable is empty.
		"""
		if(variable == "" or variable == "~"):
			print("There is no info about " + name + ".")
			return True
		return False