from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn import svm

df = pd.read_csv('../train_feat.csv')
y = df.label
x = df.drop(['uid','label'],axis=1)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

clf = svm.SVC(C=5.0)
clf.fit(x_train,y_train)
y_predict = clf.predict(x_test)
print(accuracy_score(y_test,y_predict))