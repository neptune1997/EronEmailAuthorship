import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
from sklearn.cross_validation import train_test_split
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report 
df=pd.read_csv(r"C:\Users\LPX\Desktop\bigdatam2.csv")
#df=pd.read_excel(r"C:\Users\LPX\Desktop\basic.xlsx")
index=[x for x in df.columns]
y=df.loc[:,index[-1]]
x=df.loc[:,index[0:len(index)]]
#####nomalization#####
xss=StandardScaler(with_std=True)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=33)
x_test=xss.fit_transform(x_test)
x_train=xss.transform(x_train)
######rbfSVC####
rbf=SVC(kernel='poly',degree=2)
rbf.fit(x_train,y_train)
y_predict=rbf.predict(x_test)
print "the accuracy is :",rbf.score(x_test,y_test)
print classification_report(y_test,y_predict)


