import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re

data = pd.read_csv("mainData.csv")
value_y = []
value = data["value"]

for i in range(len(value)):
	temp = value[i]
	value_y.append(temp)

c = 2000
list_of_c = []

for i in range(100):
	list_of_c.append(c)
	c+=100

k = 0.00
list_of_k = []
for i in range(100):
	list_of_k.append(k)
	k+=0.01

def Tout(tout):
	temp_tout = []
	for i in range(len(tout)):
		temp = tout[i] - tout[i-1]
		temp_tout.append(temp)
	return temp_tout

def Ti(ti,tout):
	temp_ti = []
	for i in range(len(tout)):
		temp_ti_value = ti - tout[i]
		temp_ti.append(temp_ti_value)
	return temp_ti

def grid(y):
	tout_arr = Tout(y)
	ti = Ti(23,y)
	temp_global = 0
	c_temp = 0
	global_dict = {}
	var_glob = []
	c_glob = []
	k_glob = []
	for i in range(100):
		k_temp = list_of_k[i]
		for j in range(100):
			c_temp = list_of_c[j]
			for z in range(1,len(y)-1):
				temp_global =+ c_temp*tout_arr[j] - c_temp*ti[j-1] + ti[j]*(c_temp+k_temp)
			temp_global = temp_global/(len(y)-1)
			var_glob.append(temp_global)
			c_glob.append(c_temp)
			k_glob.append(k_temp)
			global_dict = {"var":var_glob,"c":c_temp,"k":k_temp}
	return var_glob,c_glob,k_glob

def result(v,c,k):
	first = v[701]
	c_bigger = 0
	k_bigger = 0
	for i in range(700,len(v)):
		if first > v[i]:
			first = v[i]
			c_bigger = c[i]
			k_bigger = k[i]
	return first,c_bigger,k_bigger

def gloabalTemperature(tout,t):
	tout_arr = Tout(tout)

	ti = Ti(18,tout)
	ti_1 = Ti(19,tout)
	ti_2 = Ti(20,tout)

	final_array_q = []

	var,c_list,k_list = grid(tout)
	var_var,c,k =result(var,c_list,k_list) 

	temp_global_first = 23
	temp_global_second = 24
	temp_global_third = 25

	midl = (temp_global_first + temp_global_second + temp_global_third) / 3

	final_array_q.append(midl)
	for i in range(1,len(tout)-1):
		temp_global = c*tout_arr[i] - c*ti[i-1] + ti[i]*(c+k)
		temp_global_second = c*tout_arr[i] - c*ti_1[i-1] + ti_1[i]*(c+k)
		temp_global_third = c*tout_arr[i] - c*ti_2[i-1] + ti_2[i]*(c+k)
		midl = (temp_global + temp_global_second + temp_global_third )/3
		#print(temp_global_second,"\t",temp_global_third,"\t",temp_global)
		final_array_q.append(midl)
	return final_array_q

#q = gloabalTemperature(value_y,1)
# for i in range(len(q)):
#	print(q[i])