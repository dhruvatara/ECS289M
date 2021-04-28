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
	root = sys.argv[1].split("\\")
	root = root[1]+"\\"+root[2]
	# print(root)
	#Drop azimuth column
	cleanFile = file.drop(['gyro(x)'],axis=1)
	# print(cleanFile.head())
	
	# print(cleanFile['gyro(y)'][:5])
	normalize(cleanFile,'gyro(y)')
	normalize(cleanFile,'gyro(z)')
	matchup(root,cleanFile)
	cleanFile.to_csv(root+"\\cleanedGyroReadings.csv")
	# print(cleanFile['gyro(y)'][:5])
	# print(yMean)

def matchup(root,cleanGyro):
	buttonPress = pd.read_csv(root+"\\button-readings.csv")
	gyroTime = cleanGyro['timestamp']
	buttonStart = buttonPress['pressStart']
	buttonStop = buttonPress['pressStop']
	
	j = 0
	k = 0
	meanGyroY = 0.0
	meanGyroZ = 0.0
	n = 0
	# print(gyroTime[9])
	# print(buttonStart[1])
	# print(buttonStop[1])
	while (k<len(gyroTime) and j<len(buttonStop)):
		# print("here")
		if (gyroTime[k] >= buttonStart[j] and gyroTime[k]<=buttonStop[j]):
			# print("here")
			meanGyroY += cleanGyro.iloc[k]['gyro(y)']
			meanGyroZ += cleanGyro.iloc[k]['gyro(z)']
			n+=1
		elif(gyroTime[k]>buttonStop[j] and n>0):

			meanGyroY /= n
			meanGyroZ /= n
			# print(meanGyroY)
			buttonPress.at[j,'mean gyro(y)'] = meanGyroY
			buttonPress.at[j,'mean gyro(z)'] = meanGyroZ
			n = 0
			j+=1
			k-=1
		elif(gyroTime[k]>buttonStart[j]):
			j+=1
			k-=1
		k+=1
	buttonPress.to_csv(root+"\\combinedReadings.csv")


def normalize(data,column):
	#Normalize gyroscope readings
	mean = np.mean(data[column])
	data[column] = [i-mean for i in data[column]]

clean_data()
