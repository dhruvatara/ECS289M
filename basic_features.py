'''
script to extract the basic features for the classification
basic features are the angle between the direction of the upper lobe and the x-axis (AUB),
and the angle between the direction of the lower lobe and the x-axis (ALB)
'''
import pandas as pd
import sys
import math
def find_basic_features():
	root = sys.argv[1]
	file = pd.read_csv(root+"\\cleanData.csv")
	# print(file.head())
	file['AUB'] = [0.0 for _ in range(len(file))]
	file['ALB'] = [0.0 for _ in range(len(file))]
	file = file.dropna()
	calculate_angle(file)
	print(file.head())
	file.to_csv(root+'\\basicFeatures.csv',index=False)

def calculate_angle(dataset):
	for idx in dataset.index:
		# print(dataset['mean beta'][idx])
		if (dataset['mean beta'][idx] == 0):
			if (dataset['max beta'][idx] >= 0):
				dataset.at[idx,'AUB'] = math.atan(dataset['max beta'][idx]/dataset['max gamma'][idx])
			else:
				dataset.at[idx,'ALB'] = math.atan(dataset['max beta'][idx]/dataset['max gamma'][idx])
		elif (math.isnan(dataset['mean beta'][idx])):
			continue
		else:
			dataset.at[idx,'AUB'] = math.atan(math.sqrt((dataset['max beta'][idx]-dataset['mean beta'][idx])**2/(dataset['max gamma'][idx]-dataset['mean gamma'][idx])**2))
			dataset.at[idx,'ALB'] = math.atan(math.sqrt((dataset['min beta'][idx]-dataset['mean beta'][idx])**2/(dataset['min gamma'][idx]-dataset['mean gamma'][idx])**2))


if __name__ == '__main__':
	find_basic_features()