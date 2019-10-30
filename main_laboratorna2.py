import new_arima
import newq
import pandas as pd

paht_to_data = "mainData.csv"

def CountQAndArima(step,path,p,q,d=0):
	data = pd.read_csv(path)
	temp_y = []
	temp_y.extend(data['value'])
	y = []
	for i in range(len(temp_y)):
	    temp = temp_y[i]
	    y.append(temp)

	q_list = newq.gloabalTemperature(y,1)
	x = []
	for i in range(len(q_list)):
	    x.append(i)

	result = new_arima.ARIMA_with_Prediction(step=step,x=x,y=q_list,p=p,q=q,d=0)
	return result

result = CountQAndArima(2,paht_to_data,1,7)
print("Predict = ",result)