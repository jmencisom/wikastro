# -*- coding: utf-8 -*-

class BasicInfo:

	def __init__(self, attributes):
		"""
		Receives the attributes in a string and then assigns these values into
		the class variables.

		Author: Andres Linares
		Date: 2018-03-03
		Modified: 2018-03-06 By Francisco Rodríguez.
		Parameters: String that contains basic info separated by '|'
		Returns: Nothing.
		"""
		self.__attributes = attributes
		self.__objectType = ""
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

		Author: Andres Linares
		Date: 2018-03-03
		Modified: 2018-03-03 by Francisco Rodríguez.
		Parameters: Nothing.
		Returns: Nothing.
		"""
		separatedText = self.__attributes.split("|")
		self.__objectType = separatedText[3]
		self.__rightAscension = separatedText[1]
		self.__declination = separatedText[2]
		self.__helioRadialVelocity = separatedText[4]
		self.__redShift = separatedText[5]
		self.__morphologicalType = separatedText[7]
		self.__apparentMagnitude = separatedText[6]
		self.__otherNames = self.formatOtherNames(separatedText[8])


	def setAttributes(self, attributes):
		self.__attributes = attributes
		self.__obtainValues()

	def getAttributes(self):
		return self.__attributes

	def getObjectType(self):
		if(self.testEmptiness(self.__objectType, "Object Type")):
			return ""
		else:
			return self.__objectType

	def getEpoch(self):
		return self.__epoch

	def getRightAscension(self):
		if(self.testEmptiness(self.__rightAscension, "Right Ascension")):
			return ""
		else:
			return self.__rightAscension

	def getDeclination(self):
		if(self.testEmptiness(self.__declination, "Declination")):
			return ""
		else:
			return self.__declination

	def getHelioRadialVelocity(self):
		if(self.testEmptiness(self.__helioRadialVelocity,
				"Helio Radial Velocity")):
			return ""
		else:
			return self.__helioRadialVelocity

	def getRedShift(self):
		if(self.testEmptiness(self.__redShift, "Red Shift")):
			return ""
		else:
			return self.__redShift

	def getMorphologicalType(self):
		if(self.testEmptiness(self.__morphologicalType, "Morphological Type")):
			return ""
		else:
			return self.__morphologicalType

	def getApparentMagnitude(self):
		if(self.testEmptiness(self.__apparentMagnitude, "Apparent Magnitude")):
			return ""
		else:
			return self.__apparentMagnitude

	def getOtherNames(self):
		if(self.testEmptiness(self.__otherNames, "Other Names")):
			return ""
		else:
			return self.__otherNames

	def getCoordinates(self):
		"""
		This method concatenates the right ascension and the declination
		into a single string.

		Author: Andres Linares
		Date: 2018-03-03
		Modified: Never.
		Parameters: Nothing.
		Returns: Coordinates in the form: right_ascension declination.
		"""
		return (self.getRightAscension() + " " + self.getDeclination()).split()


	def formatOtherNames(self, names):
		"""
		This method checks that the main name is not included and also 
		adds the known references.

		Author: Francisco Rodriguez
		Date: 2018-03-06
		Modified: Never.
		Parameters: A string that contains the list of names returned by simbad.
		Returns: A String that contains the referenced names.
		"""
		format_names=names[names.find(",")+1:] #elimina primer nombre (NGC)
		for ref in self.__namesReferences:
			#format_names.replace(ref[0], ref[1]) ideal, pero no está funcionando
			inicio = format_names.find(ref[0])
			if (inicio>=0):
				sub1 = format_names[:inicio]
				format_names = sub1 + ref[1] + format_names[inicio+len(ref[0]):]
		return format_names

	def testEmptiness(self, variable, name):
		"""
		This method test the emptiness of a variable. The emptiness is
		represented by a empty string '' or by this string: '~'. If
		the variable is empty then True is returned.

		Author: Andres Linares.
		Date: 2018-03-03
		Modified: Never.
		Parameters: Variable to test and name of the variable to print.
		Returns: True if variable is empty.
		"""
		if(variable == "" or variable == "~"):
			print("There is no info about " + name + ".")
			return True
		return False