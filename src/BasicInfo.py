# -*- coding: utf-8 -*-

class BasicInfo:

	def __init__(self, attributes):
		"""
		Receives the attributes in a string and then assigns these values into
		the class variables.

		Author: Andres Linares
		Date: 2018-03-03
		Modified: Never.
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
		self.__obtainValues()



	def __obtainValues(self):
		"""
		Using the variable 'self.__attributes', a string array is obtained
		and then each individual string is assigned to differents
		clas variables.

		Author: Andres Linares
		Date: 2018-03-03
		Modified: Never.
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
		self.__otherNames = separatedText[8].replace(",",u"·")


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
		if(self.testEmptiness(self.__apparentMagnitude, "Other Names")):
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