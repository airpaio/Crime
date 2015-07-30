# Python script to scrape all .xls (Excel Spreadsheet) files from the 
#	indicated website.

import urllib
from bs4 import BeautifulSoup
import os

# Here we want to scrape .xls files of daily crime stats in Houston, TX
#	from 2009 to 2014.
url = "http://www.houstontx.gov/police/cs/stats2.htm"
url2 = "http://www.houstontx.gov/police/cs/xls/"
req = urllib.urlopen(url) 		# navigates to the url

soup = BeautifulSoup(req)

# Find each <a href="...">XLS</a> and download the file pointed to by href="..."
count = 0
for link in soup.findAll('a'):
	if link.string == 'Excel Spreadsheet':
		webFile, fileExtension = os.path.splitext(link.get('href'))
		fileName = webFile.split("/")[-1]
		saveAs = os.path.join("data/", fileName + fileExtension)
		print("Retreiving " + fileName + fileExtension)
		urlFile = url2 + fileName + fileExtension
		urllib.urlretrieve(urlFile, saveAs)
		count += 1

print("Successfully retrieved ", count, " files") 




"""
location = "http://www.houstontx.gov/police/cs/stats2.htm"
page = urllib.urlopen(location)
soup = BeautifulSoup(page)
 
# Find each <a href="...">XLS</a> and download the file pointed to by href="..."
for link in soup.findAll('a'):
    if link.string == 'Excel Spreadsheet':
        filename = link.get('href')
        print("Retrieving " + filename)
    	url = location + filename
        urllib.urlretrieve(url,filename)
"""
