#script to clean the data to extract features as outlined in Touchlogger
"""
1. discard azimuth angle since typing mostly affects pitch and roll angles
2. normalize the angles by finding mean of angles and subtracting
3. combine the two CSVs
"""

import sys
import pandas as pd
import numpy as np
def clean_data():
	file = pd.read_csv(sys.argv[1])
	# print(file.head())
	#Drop azimuth column
	cleanFile = file.drop(['gyro(x)'],axis=1)
	# print(cleanFile.head())
	
	# print(cleanFile['gyro(y)'][:5])
	normalize(cleanFile,'gyro(y)')
	normalize(cleanFile,'gyro(z)')
	# print(cleanFile['gyro(y)'][:5])
	# print(yMean)

def normalize(data,column):
	#Normalize gyroscope readings
	mean = np.mean(data[column])
	data[column] = [i-mean for i in data[column]]

clean_data()
