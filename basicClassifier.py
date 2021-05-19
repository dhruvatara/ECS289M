'''
script to train, test and validate different classifiers
'''
import sys
import pandas as pd
from sklearn.linear_model import RidgeClassifier, LogisticRegression, SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
def main():
	root = sys.argv[1]
	path = root+'\\basicFeatures.csv'
	# print(path)
	data = pd.read_csv(path)
	# print(data.head())
	X = data[['max beta','max gamma']]
	print(X.head())
	Y = data['label']
	xtrain,xtest,ytrain,ytest = train_test_split(X,Y,test_size=0.3)
	nbClassifier = GaussianNB().fit(xtrain,ytrain)
	ypred = nbClassifier.predict(xtest)
	print("Naive Bayes Test accuracy: ",metrics.accuracy_score(ytest,ypred))
	ridClassifier = RidgeClassifier().fit(xtrain,ytrain)
	ypred = ridClassifier.predict(xtest)
	print("Ridge Classifier Test accuracy: ",metrics.accuracy_score(ytest,ypred))
	logRes = LogisticRegression(multi_class='multinomial',solver='sag').fit(xtrain,ytrain)
	ypred = logRes.predict(xtest)
	print("Logistic Regression Test accuracy: ",metrics.accuracy_score(ytest,ypred))
	sgdClassifier = SGDClassifier(max_iter=1000).fit(xtrain,ytrain)
	ypred = sgdClassifier.predict(xtest)
	print("SGD Classifier Test accuracy: ",metrics.accuracy_score(ytest,ypred))
	dtClassifier = DecisionTreeClassifier().fit(xtrain,ytrain)
	ypred = dtClassifier.predict(xtest)
	print("Decision Tree Test accuracy: ",metrics.accuracy_score(ytest,ypred))
	rfClassifier = RandomForestClassifier().fit(xtrain,ytrain)
	ypred = rfClassifier.predict(xtest)
	print("Random Forest Test accuracy: ",metrics.accuracy_score(ytest,ypred))
	
	return

if __name__ == '__main__':
	main()