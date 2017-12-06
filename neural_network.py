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
model.add(Dense(12,input_dim=8,kernel_initializer="uniform",activation="relu"))
model.add(Dense(8,activation="relu"))
model.add(Dense(1,activation="sigmoid"))
#Now we need to compile the model
model.compile(loss="binary_crossentropy",optimizer="adam",metrics=["accuracy"])
#Now we need to execute the model
model.fit(x,y,epochs=150,batch_size=10)
#Now we need to evaluate the model
scores=model.evaluate(x,y)
print("\n The accuracy is {0}%" .format(round(scores[1]*100),2))
