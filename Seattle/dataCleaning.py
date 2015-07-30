import numpy as np
import pandas as pd
import re
import warnings
import timeit

# read in the raw csv
# got warnings about mixed data types... here is a fix to try loading the data as a str
targetType = str   # data type we want to force

with warnings.catch_warnings(record=True) as ws:
	warnings.simplefilter("always")

	dat = pd.read_csv('data/seaPD911IR.csv')
	print("Warnings raised: ", ws)
	# try loading the columns with the warnings as strings
	for w in ws:
		s = str(w.message)
		print("Warning message: ", s)
		match = re.search(r"Columns \(([0-9,]+)\) have mixed types\.", s)
		if match:
			columns = match.group(1).split(',')   # get columns as a list
			columns = [int(c) for c in columns]
			print("Applying %s dtype to columns: " % targetType, columns)
			dat.iloc[:,columns] = dat.iloc[:,columns].astype(targetType)


df = pd.DataFrame(dat)

# rename the columns of the dataframe
df.rename(columns={'CAD CDW ID':'cadCdwID', 'CAD Event Number':'cadEvntNum', 
                   'General Offense Number':'genOffenseNum', 'Event Clearance Code':'clearCode',
                  'Event Clearance Description':'clearDiscript', 
                   'Event Clearance SubGroup':'clearSubGrp',
                   'Event Clearance Group':'clearGrp', 'Event Clearance Date':'clearDate',
                  'Hundred Block Location':'blockLoc', 'District/Sector':'district', 
                   'Zone/Beat':'beat', 'Census Tract':'censusTract', 'Longitude':'lon', 
                   'Latitude':'lat', 'Incident Location':'loc', 
                   'Initial Type Description':'initDescript', 
                   'Initial Type Subgroup':'initSubGrp', 'Initial Type Group':'initGrp',
                  'At Scene Time':'timeAtScene'}, inplace=True)


# we want...
# 0 to be int
try:
	df.iloc[:,0] = df.iloc[:,0].astype(int)
except ValueError:
	
# 12 to be float
df.iloc[:,12] = df.iloc[:,12].astype(float)
# 15 to be str
# 16 to be str
# 17 to be str
# 18 to be datetime
print("converting to datetime...")
timeit(pd.to_datetime(df.iloc[:,18]))


"""
df = df.drop('loc',1)

df = df.dropna(subset=['clearDate'])

df = df.dropna(subset=['lon'])
df = df.dropna(subset=['lat'])

df = df.dropna(subset=['timeAtScene'])

# convert the time strings to datetime objects
df['timeAtScene'] = pd.to_datetime(df['timeAtScene'])
df['clearDate'] = pd.to_datetime(df['clearDate'])

from datetime import datetime

df = df.set_index(['timeAtScene'])

print df.head()
"""