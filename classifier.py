'''
script to train, test and validate a gaussian naive bayes classifier
'''
import sys
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
def main():
	root = sys.argv[1]
	path = root+'\\basicFeatures.csv'
	# print(path)
	data = pd.read_csv(path)
	# print(data.head())
	X = data.drop(['label','pressStart','pressStop'],axis=1)
	Y = data['label']
	xtrain,xtest,ytrain,ytest = train_test_split(X,Y,test_size=0.3)
	classifier = GaussianNB().fit(xtrain,ytrain)
	ypred = classifier.predict(xtest)
	print("Test accuracy: ",metrics.accuracy_score(ytest,ypred))
	return

if __name__ == '__main__':
	main()