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

