from keras.models import Sequential
from keras.layers import Dense 
import numpy
#Set the random seed so we can reproduce the results
numpy.random.seed(7)
#Load the dataset for the pima indians
data_set=numpy.loadtxt("pima-indians-diabetes.csv",delimiter=",")
#split the dataset into x and y variables
x=data_set[:,0:8]
y=data_set[:,8]
#Now we need to create the model
model=Sequential()
model.add(Dense(12,input_dim=8,init="uniform",activation="relu"))
model.add(Dense(8,activation="relu"))
model.add(Dense(1,activation="sigmoid"))