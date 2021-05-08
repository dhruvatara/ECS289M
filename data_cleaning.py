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
	root = sys.argv[1]
	path = root+"\\gyro-readings.csv"
	file = pd.read_csv(path)
	# print(file.head())
	
	# print(root)
	#Drop azimuth column
	file.columns = ['timestamp','beta','gamma','alpha']
	cleanFile = file.drop(['alpha'],axis=1)
	print(cleanFile.head())
	
	# print(cleanFile['gyro(y)'][:5])
	normalize(cleanFile,'beta')
	normalize(cleanFile,'gamma')
	matchup(root,cleanFile)
	# cleanFile.to_csv(root+"\\cleanedGyroReadings.csv")
	# print(cleanFile['gyro(y)'][:5])
	# print(yMean)

def matchup(root,cleanGyro):
	buttonPress = pd.read_csv(root+"\\button-readings.csv")
	gyroTime = cleanGyro['timestamp']
	buttonStart = buttonPress['pressStart']
	buttonStop = buttonPress['pressStop']
	
	j = 0
	k = 0
	meanBeta = 0.0
	minBeta = 0.0
	maxBeta = 0.0
	meanGamma = 0.0
	minGamma = 0.0
	maxGamma = 0.0
	maxDistUp = 0.0
	maxDistDown = 0.0
	dist = 0.0
	n = 0
	# print(gyroTime[9])
	# print(buttonStart[1])
	# print(buttonStop[1])
	while (k<len(gyroTime) and j<len(buttonStop)):
		# print("here")
		if (n==0):

			minBeta = cleanGyro.iloc[k]['beta']
			minGamma= cleanGyro.iloc[k]['gamma']
			maxBeta = cleanGyro.iloc[k]['beta']
			maxGamma = cleanGyro.iloc[k]['gamma']
			maxDistUp = 0.0
			maxDistDown = 0.0
			dist = 0.0
			# maxSlopeUp = (maxBeta**2/maxGamma**2)**0.5
		if (gyroTime[k] >= buttonStart[j] and gyroTime[k]<=buttonStop[j]):
			# print("here")
			meanBeta += cleanGyro.iloc[k]['beta']
			meanGamma += cleanGyro.iloc[k]['gamma']
			dist = (cleanGyro.iloc[k]['beta']**2+cleanGyro.iloc[k]['gamma']**2)**0.5
			if(cleanGyro.iloc[k]['beta'] < 0 and dist > maxDistDown):
				minBeta = cleanGyro.iloc[k]['beta']
				minGamma = cleanGyro.iloc[k]['gamma']
				maxDistDown = dist
			elif (cleanGyro.iloc[k]['beta'] > 0 and dist > maxDistUp):
				maxBeta = cleanGyro.iloc[k]['beta']
				maxGamma = cleanGyro.iloc[k]['gamma']
				maxDistUp = dist
			n+=1
			# cleanGyro.at[k,'label'] = buttonPress.iloc[j]['label']
		elif(gyroTime[k]>buttonStop[j] and n>0):

			meanBeta /= n
			meanGamma /= n
			buttonPress.at[j,'max beta'] = maxBeta
			buttonPress.at[j,'max gamma'] = maxGamma
			buttonPress.at[j,'min beta'] = minBeta
			buttonPress.at[j,'min gamma'] = minGamma
			
			# print(meanGyroY)
			if(n == 1):
				buttonPress.at[j,'mean beta'] = 0.0
				buttonPress.at[j,'mean gamma'] = 0.0
			else:
				buttonPress.at[j,'mean beta'] = meanBeta
				buttonPress.at[j,'mean gamma'] = meanGamma
			
			n = 0
			meanBeta = 0.0
			minBeta = 0.0
			maxBeta = 0.0
			meanGamma = 0.0
			minGamma = 0.0
			maxGamma = 0.0
			j+=1
			k-=1
		elif(gyroTime[k]>buttonStart[j]):
			j+=1
			k-=1
		k+=1
	buttonPress.to_csv(root+"\\cleanData.csv",index=False)


def normalize(data,column):
	#Normalize gyroscope readings
	print(column)
	mean = np.mean(data[column])
	print(mean)
	data[column] = [i-mean for i in data[column]]

if __name__ == '__main__':
	clean_data()