
# coding: utf-8

# In[ ]:


from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import math

df = pd.read_csv('../train_feat.csv')
y = df.label
x = df.drop(['uid','label'],axis=1)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

def my_weights(distance):
    a = 1
    b = 0
    c = 0.3
    power_matrix = -np.square(distance - b) / (2 * c ** 2)
    return a * np.power(math.e,power_matrix)

knn = KNeighborsClassifier(n_neighbors=300,weights=my_weights)
knn.fit(x_train,y_train)
y_predict = knn.predict(x_test)
print(accuracy_score(y_test,y_predict))

