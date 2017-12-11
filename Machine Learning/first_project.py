#First we need to load all of the libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
#Now we need to load all of the data
url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names=["sepal-length","sepal-width","petal-length","petal-witdh","class"]
dataset=pandas.read_csv(url,names=names)
#Now we need to get the dimension of the dataset
#print(dataset.shape)
################################################
#Now we need to look at the first 20 rows of data
#print(dataset.head(20))
#Now we need to get the statistical summary of the data
#print(dataset.describe())
#Now we need to find the number of instances that belong to each class
#print("The number of instances in each class is {0}".format(dataset.groupby("class").size()))
#Now we need to visualize the data
#We will generate a box and whisker plot
#dataset.plot(kind="box",subplots=True,layout=(2,2),sharex=False,sharey=False)
#plt.show()
#Now we need to create a histogram of each input variable to see what we get
#dataset.hist()
#plt.show()
#Now we need to look at the interactions between the variables
#scatter_matrix(dataset)
#plt.show()
#Most of the interaction with the variables has a predfictable correlation
#now we need to create the model(1.create the validation dataset)
#Splitting out validation dataset
my_array=dataset.values
#print(my_array)
#Splitting the data into the x and the y values
X=my_array[:,0:4]
Y=my_array[:,4]
#Now we need to set the validation size and the seed  for preparing the models
validation_size=.2
seed=7
#We will use 20 percent of our data  for validation
