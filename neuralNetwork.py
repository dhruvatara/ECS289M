'''
Accuracy of classifiers so far has been underwhelming (< 30%), so hopefully a NN will be able to do better
'''
import sys
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from keras.layers import InputLayer, Dense
from sklearn.model_selection import train_test_split
from sklearn import metrics
def main():
	root = sys.argv[1]
	path = root+'\\basicFeatures.csv'
	# print(path)
	data = pd.read_csv(path)
	X = data[['max beta','max gamma']]
	Y = data['label']
	print(X.shape)
	print(Y.shape)
	xtrain,xtest,ytrain,ytest = train_test_split(X,Y,test_size=0.3)
	model = keras.Sequential()
	# model.add(InputLayer(input_shape=(2,)))
	model.add(Dense(8,input_shape=(2,),activation='relu'))
	# model.add(Dense(16))
	model.add(Dense(10,activation='softmax'))
	model.compile(loss='categorical_crossentropy',optimizer='sgd',metrics=['accuracy','precision','recall'])
	# print(tf.keras.utils.plot_model(model))
	model.fit(xtrain,ytrain,
		epochs=2)

if __name__ == '__main__':
	main()