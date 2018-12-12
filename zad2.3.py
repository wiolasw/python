#!/usr/bin/python
from random import randint
from xml.dom.minidom import parse
import xml.dom.minidom


DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
movies = collection.getElementsByTagName("movie")


for movie in movies:
   print("-----------MOVIE------------------------")
   title = movie.getElementsByTagName('title')[0]
   print ("Title: %s" % title.childNodes[0].data)
   type = movie.getElementsByTagName('type')[0]
   print ("Type: %s" % type.childNodes[0].data)


   import xml.etree.ElementTree as ET

   tree = ET.parse('movies.xml')
   root = tree.getroot()

   attrib = {'OUT_OF_STOCK': '-----------YES-----------'}
   for i in range (0, (randint(1,5))):
       subelement = root[0][0].makeelement('availability', attrib)
       ET.SubElement(root[i], 'Availability', attrib)

   tree.write('out.xml')

