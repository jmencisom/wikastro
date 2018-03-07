# -*- coding: utf-8 -*-

import urllib as url_op
import json
import datetime
from bs4 import BeautifulSoup

class Image_NGC:

	def __init__(self, name):
		self.__name = name

	def getImage(self):
		"""
		This method seeks for the more recent image in Wikimedia Commons
		and obtains the file name.

		Author: Andres Linares
		Date: 2018-03-06
		Modified: Never.
		Parameters: Nothing
		Returns: Image file name.
		"""
		json = self.__obtainPage()
		images = json["query"]["search"]
		index = self.__getIndexNewerImage(images)
		return images[index]["title"][5:]

	def getCaption(self, image):
		pass

	def __getIndexNewerImage(self, json):
		"""
		This method gets the index of the newer image using the
		timestamp attribute on the json.

		Author: Andres Linares
		Date: 2018-03-06
		Modified: Never.
		Parameters: json that contains the search result list.
		Returns: Index of the newer image.
		"""
		greater = json[0]["timestamp"]
		indexGreater = 0
		for x in range(1, len(json)):
			isGreater = self.__compareDates(greater, json[x]["timestamp"])
			if(isGreater):
				greater = json[x]["timestamp"]
				indexGreater = x
		return indexGreater




	def __compareDates(self, a, b):
		"""
		This methods recieves two dates (strings) and compares dates.
		This methods returns true if b is greater than a.

		Author: Andres Linares
		Date: 2018-03-06
		Modified: Never.
		Parameters: Date a and Date b encoded as strings
		Returns: True or False
		"""
		dateTextA = a[:10]
		dateTextB = b[:10]
		dateTextA = dateTextA.split("-")
		dateTextB = dateTextB.split("-")
		dateA = datetime.date(int(dateTextA[0]), int(dateTextA[1]),
		 		int(dateTextA[2]))
		dateB = datetime.date(int(dateTextB[0]), int(dateTextB[1]),
				int(dateTextB[2]))
		return dateB > dateA



	def __obtainPage(self):
		"""
		This method uses the wikimedia api to obtain a search result list
		ob an NGC Object. It will obtain a json and will return it

		Author: Andres Linares
		Date: 2018-03-06
		Modified: Never.
		Parameters: Nothing.
		Returns: json with search result list.
		"""
		url = ("https://commons.wikimedia.org/w/api.php?action=query" +
			"&list=search&srnamespace=6&srsearch=%22ngc+394%22&format=json")
		name = self.__name.replace(" ", "+")
		url = url.replace("ngc+394", name)
		response = url_op.urlopen(url)
		return json.load(response)