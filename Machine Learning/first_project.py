#First we need to load all of the libraries
import pandas
from pandas.tools.plotting import scatter_matrix
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

