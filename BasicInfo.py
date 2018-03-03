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


	def setAttributes(self, attributes):
		self.__attributes = attributes
		self.__obtainValues()

	def getAttributes(self):
		return self.__attributes

	def getObjectType(self):
		return self.__objectType

	def getEpoch(self):
		return self.__epoch

	def getRightAscension(self):
		return self.__rightAscension

	def getDeclination(self):
		return self.__declination

	def getHelioRadialVelocity(self):
		return self.__helioRadialVelocity

	def getRedShift(self):
		return self.__redShift

	def getMorphologicalType(self):
		return self.__morphologicalType

	def getApparentMagnitude(self):
		return self.__apparentMagnitude

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
		return (self.__rightAscension + " " + self.__declination).split()