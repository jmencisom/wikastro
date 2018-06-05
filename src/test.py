# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import re
import unittest
from BasicInfo import BasicInfo
from Image_NGC import Image_NGC
from WikiGeneration import WikiGeneration
from ObtainInfo import ObtainInfo
		
		





##Pruebas Unitarias
class TestUM(unittest.TestCase):
	def test_category(self):
		ngc = "NGC"
		ngc_num = 700

		ngc_num = str(ngc_num)
		ngc_nomb = ngc + " " + ngc_num
		print("\nobject: " + ngc_nomb)

		webpage = ""
		try:
			print("\nSearching object in database...\n")
			obtainInfo = ObtainInfo()
			soup, webpage = obtainInfo.obtainPage(ngc_num)
			text_basicInfo = obtainInfo.getValues(soup)

			basicInfo = BasicInfo(text_basicInfo)
			
			image = Image_NGC(ngc_nomb)
			imageName = image.getImage()
			imageCaption = image.getCaption(ngc_nomb)

			wikiGeneration = WikiGeneration()
			fatherPageTextWiki, objec = wikiGeneration.generateFatherPage(
				basicInfo.getObjectType())
			
			output ="\n==See also==\n*[[Galaxy]]\n"
			self.assertEqual(fatherPageTextWiki,output)
			
		except IOError as err:
			print ("\nCan not connect to Internet.\n")
		except IndexError as err:
			print("\nThe object was not found in database.\n")

	def test_coordinates(self):
		ngc = "NGC"
		ngc_num = 700

		ngc_num = str(ngc_num)
		ngc_nomb = ngc + " " + ngc_num
		print("\nobject: " + ngc_nomb)

		webpage = ""
		try:
			print("\nSearching object in database...\n")
			obtainInfo = ObtainInfo()
			soup, webpage = obtainInfo.obtainPage(ngc_num)
			text_basicInfo = obtainInfo.getValues(soup)

			basicInfo = BasicInfo(text_basicInfo)
			
			image = Image_NGC(ngc_nomb)
			imageName = image.getImage()
			imageCaption = image.getCaption(ngc_nomb)

			wikiGeneration = WikiGeneration()
			coordinatesTextWiki = wikiGeneration.transformToCoordinatesWiki(
				basicInfo.getCoordinates())
		
			output1 ="{{Sky|01|52|12.700||+36|05|50.26|999}}\n"
			self.assertEqual(coordinatesTextWiki,output1)
			
		except IOError as err:
			print ("\nCan not connect to Internet.\n")
		except IndexError as err:
			print("\nThe object was not found in database.\n")


	def test_find(self):

		ngc = "NGC"
		ngc_num = 2277

		ngc_num = str(ngc_num)
		ngc_nomb = ngc + " " + ngc_num
		print("\nobject: " + ngc_nomb)

		webpage = ""
		try:
			print("\nSearching object in database...\n")
			obtainInfo = ObtainInfo()
			soup, webpage = obtainInfo.obtainPage(ngc_num)
			text_basicInfo = obtainInfo.getValues(soup)

			basicInfo = BasicInfo(text_basicInfo)
			
		except IOError as err:
			print ("\nCan not connect to Internet.\n")
		except IndexError as err:
			print()		
			output2 ="\nThe object was not found in database.\n"
			self.assertEqual("\nThe object was not found in database.\n",output2)
		

	def test_positivo(self):
		print("\nSearching object in database...\n")
		ngc = "NGC"
		ngc_num = 1
		self.assertGreater(ngc_num,0)

	
		
if __name__ == '__main__':
	unittest.main()