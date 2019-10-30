import pandas as pd

data = pd.read_csv("KiberLaoratorna2Temperature/full_external_temperatures.csv")
time = data["dateTime"]
value = data["data"]

time_x = []
value_y = []

for i in range(28804,29100):#35135):
	temp_time = time[i]
	temp_value = value[i]
	time_x.append(temp_time)
	value_y.append(temp_value)
new_data = pd.DataFrame({"value":value_y})
new_data.to_csv("mainData.csv")

new_data = pd.read_csv("mainData.csv")
value_y = new_data["value"]
for i in range(len(value_y)):
	print(value_y[i])