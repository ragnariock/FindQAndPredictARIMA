import read_file
import q
import arima

array = read_file.read_return_arr()
q_list = q.gloabalTemperature(array,1)

x = []
for i in range(len(q_list)):
    x.append(i)

for i in range(len(q_list)):
    print("Q[{0}] = {1}".format(i,q_list[i]))

# print(ARIMA_with_Prediction(2,x,y,p=1,q=7,d=0))
arima_result = arima.ARIMA_with_Prediction(2,x,q_list,p=1,q=6,d=0)
print("============================================================")
print("RESULT ARIMA = {0}".format(arima_result))
