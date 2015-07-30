import pandas as pd
import os
import xlrd

successCount = 0
errorCount = 0
conversionCount = 0
for file in os.listdir('data'):
	fileName, fileExtension = os.path.splitext(file)
	print("Attempting to read " + file)
	try:
		data_xls = pd.read_excel("data/" + file)
		print("Successfully read " + file)
		successCount += 1
	except xlrd.XLRDError:
		print("BOF Error in file " + file)
		errorCount += 1
	
	print("Converting " + file + " to a .csv")
	data_xls.to_csv("data/" + fileName + '.csv', encoding='utf-8')   # 
	conversionCount += 1

print "%d successful reads " % successCount
print "%d erroneous reads " % errorCount
print "%d successful .csv conversions! " % conversionCount
