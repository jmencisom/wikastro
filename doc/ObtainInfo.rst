# -*- coding: utf-8 -*-

import urllib as url_op
from bs4 import BeautifulSoup

class ObtainInfo:

	def __init__(self):
		"""
		There is no need to initialize the class with any variables.
		"""
		pass


	def getValues(self, soup):
		"""
		Using get_text() method from BeautifulSoup you get a lot of spaces
		and new line characters, then is required to get rid of them to
		ease the obtaining labor later.

		
		:Param: BeautifulSoup object
		:Returns: String that contains all the meaning data (basic info in simbad
		         database).
		:rtype: String		 
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


	def obtainPage(self, ngc_num):
		"""
		Search a NGC object in simbad database and then returns the query in its
		full html page.  The search could be empty. This method uses urllib library.

		
		:Param: Integer encapsulated as a string.
		:Returns: BeautifulSoup object encoded in 'lxml'
		:rtype: lxml
		"""
		searchingPt1 = ("http://simbad.u-strasbg.fr/simbad/sim-script?submit=" +
			"submit+script&script=format+object+form1+%22%25IDLIST%281%29" +
			"%7C%25COO%28%3BA%3BJ2000%29%7C%25COO%28%3BD%3BJ2000%29%7C+%25OTYPE" +
			"%28V%29%7C%25RV%28V%29%7C%25RV%28Z%29%7C%25FLUXLIST%28B%3B+F%29%7C" +
			"%25MT%28M%29%7C%25IDLIST%28SA%28%2c%20%29%3B%29%7C%22%0D%0A" +
			"query+id+ngc+")
		searchingPt2 = "%0D%0A"
		searchingWord = searchingPt1 + ngc_num + searchingPt2

		searchingURL1 = "http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=NGC+"
		searchingURL2 = "&submit=SIMBAD+search"
		searchingURLWord = searchingURL1 + ngc_num + searchingURL2
		webpage = searchingURLWord

		searchingPage = url_op.urlopen(searchingWord)
		return BeautifulSoup(searchingPage, "lxml"), webpage
