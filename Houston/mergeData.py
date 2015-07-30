"""
Script to merge multiple .csv files into one master.csv file.
"""
import os
import csv
import numpy as np
import pandas as pd



def getHeaders(directory):
	"""
	This function returns a list of unique headers found in the directory of
	.csv files passed in as an argument.	
	First loop thru directory and get original headers for *.csv	
	"""	
	head = []
	for fileName in os.listdir(directory):
	    f = open(directory + fileName, 'rb')
	    reader = csv.reader(f)
	    headers = reader.next()
	    head.extend(headers)
	
	# now convert to np array to make use of unique() and get the unique headers
	npHead = np.array(head)
	uniqueHeaders = list(np.unique(npHead))
	return uniqueHeaders




def elemInValueList(dic, string):
    """
    This function determines if a particular string (header value) is found
    in any list within the values of the dictionary keys.
    Input:
        dic - a dictionary
        string -  a string you want to find within the values of the 
            dictionary.
    Returns:
        True - if 'string' is found
        False - otherwise
    """
    values = dic.values()
    TorF = string in [x for v in values for x in v if type(v) == list] \
        or string in values \
        or string in dic.keys()
    return TorF




def valueIndex(dic, string):
	"""
	determine the index of the vlaue list the header string is in
	"""
	if elemInValueList(dic, string):
		index = next((i for i, sublist in enumerate(dic.values()) \
			if string in sublist))
		return index
	else:
		print "%s is not in any key values" % string
		return -1




# TODO:
# rename headers in *.csv to the unique dictionary keys
def getBadHeaders(directory, dictionary):
    badHeaders = []
    for fileName in os.listdir(directory):
		f = open(directory + fileName, 'rb')
		reader = csv.reader(f)
		headers = reader.next()
		for header in headers:
		    if elemInValueList(dictionary, header) == False:
		        badHeaders.extend(header)
    return badHeaders




# merge all files in directory into one .csv file
def mergeFiles(origDirectory, destDirectory):
    print "merging files into one master data file..."
    frame = pd.DataFrame()
    list = []
    for fileName in os.listdir(origDirectory):
        df = pd.read_csv(origDirectory + fileName, index_col=0, header=0)
        list.append(df)
    frame = pd.concat(list)
    frame.to_csv(destDirectory + 'masterData.csv', sep=',', encoding='utf-8')
