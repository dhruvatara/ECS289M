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
	minGyroY = 0.0
	maxGyroY = 0.0
	meanGyroZ = 0.0
	minGyroZ = 0.0
	maxGyroZ = 0.0
	n = 0
	# print(gyroTime[9])
	# print(buttonStart[1])
	# print(buttonStop[1])
	while (k<len(gyroTime) and j<len(buttonStop)):
		# print("here")
		if (n==0):
			minGyroY = cleanGyro.iloc[k]['gyro(y)']
			minGyroZ = cleanGyro.iloc[k]['gyro(z)']
			maxGyroY = cleanGyro.iloc[k]['gyro(y)']
			maxGyroZ = cleanGyro.iloc[k]['gyro(z)']
		if (gyroTime[k] >= buttonStart[j] and gyroTime[k]<=buttonStop[j]):
			# print("here")
			meanGyroY += cleanGyro.iloc[k]['gyro(y)']
			meanGyroZ += cleanGyro.iloc[k]['gyro(z)']
			if(cleanGyro.iloc[k]['gyro(y)'] < minGyroY):
				minGyroY = cleanGyro.iloc[k]['gyro(y)']
				minGyroZ = cleanGyro.iloc[k]['gyro(z)']
			elif (cleanGyro.iloc[k]['gyro(y)'] > maxGyroY):
				maxGyroY = cleanGyro.iloc[k]['gyro(y)']
				maxGyroZ = cleanGyro.iloc[k]['gyro(z)']
			n+=1
			# cleanGyro.at[k,'label'] = buttonPress.iloc[j]['label']
		elif(gyroTime[k]>buttonStop[j] and n>0):

			meanGyroY /= n
			meanGyroZ /= n
			# print(meanGyroY)
			buttonPress.at[j,'mean gyro(y)'] = meanGyroY
			buttonPress.at[j,'mean gyro(z)'] = meanGyroZ
			buttonPress.at[j,'max gyro(y)'] = maxGyroY
			buttonPress.at[j,'max gyro(z)'] = maxGyroZ
			buttonPress.at[j,'min gyro(y)'] = minGyroY
			buttonPress.at[j,'min gyro(z)'] = minGyroZ
			n = 0
			meanGyroY = 0.0
			minGyroY = 0.0
			maxGyroY = 0.0
			meanGyroZ = 0.0
			minGyroZ = 0.0
			maxGyroZ = 0.0
			j+=1
			k-=1
		elif(gyroTime[k]>buttonStart[j]):
			j+=1
			k-=1
		k+=1
	buttonPress.to_csv(root+"\\features.csv")


def normalize(data,column):
	#Normalize gyroscope readings
	mean = np.mean(data[column])
	data[column] = [i-mean for i in data[column]]

clean_data()
