import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd  
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import export_graphviz 

# Type, cost, profit
dataset = np.array( 
[['Video', 100, 1000], 
['Clip', 500, 3000], 
['Short film', 1500, 5000], 
['Author film', 3500, 8000], 
['Horror', 5000, 6500], 
['Western', 6000, 7000], 
['Arthouse', 8000, 15000], 
['Sport film', 9500, 20000], 
['Thriller', 12000, 21000], 
['Fantasy', 14000, 25000], 
['Soup opera', 15500, 27000], 
['Comedy', 16500, 30000], 
['Sci-FI', 25000, 52000], 
['Blockbaster', 30000, 80000] 
]) 

print(dataset) 
X = dataset[:, 1:2].astype(int) 
y = dataset[:, 2].astype(int)

regressor = DecisionTreeRegressor(random_state = 0) 
regressor.fit(X, y) 
   
export_graphviz(regressor, out_file ='tree.dot', 
               feature_names =['Production Cost'])  

while True:
    print("Input price for prediction or 'exit' to exit")
    val_to_pred = input()
    if (val_to_pred == 'exit'): break
    else:
        y_pred = regressor.predict([[val_to_pred]]) 
        print("Predicted profit: % d\n"% y_pred) 