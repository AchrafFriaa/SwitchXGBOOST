import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, accuracy_score
import dataCollection

df = pd.read_csv("data.txt", index_col=0)



X_train, X_test, y_train, y_test = train_test_split(
            df.iloc[:,1:].values, df.iloc[:,0].values, test_size=0.2, stratify = df.iloc[:,0].values)

D_train = xgb.DMatrix(X_train, label=y_train)
D_test = xgb.DMatrix(X_test, label=y_test)

param = {
    'eta': 0.3, 
    'max_depth': 3,  
    'objective': 'multi:softprob',  
    'num_class': 16} 
steps = 20

model = xgb.train(param, D_train, steps)



preds = model.predict(D_test)
best_preds = np.asarray([np.argmax(line) for line in preds])

print("Precision = {}".format(precision_score(y_test, best_preds, average='macro')))
print("Recall = {}".format(recall_score(y_test, best_preds, average='macro')))
print("Accuracy = {}".format(accuracy_score(y_test, best_preds)))


label = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
while True:
    combination = dataCollection.testData()
    combination_Dmat = xgb.DMatrix(combination)
    combination_pred = model.predict(combination_Dmat)
    best_pred_combination = np.asarray([np.argmax(line) for line in combination_pred])
    best_pred_combination
    print('Current combination is : %s' %((label[best_pred_combination[0]])))