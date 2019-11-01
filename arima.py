from sympy import symbols, diff
import re
import numpy as np
import pandas as pd

import math

def minMNK(a,b):
    function = 0
    w0, w1 = symbols('x y', real=True)
    
    for i in range(len(a)):
        function +=(w1*a[i] + w0 - b[i]) ** 2
        
    #print(function)
    
    function1W0 = diff(function,w0)
    function2W1 = diff(function,w1)
        
    #print(function1W0)
   # print(function2W1)
    
    function1W0 = str(function1W0)
    function2W1 = str(function2W1)
    

    result1 = re.findall(r'\d+',function1W0)
    result2 = re.findall(r'\d+',function2W1)
    
    for i in range(len(result1)):
        result1[i] = int(result1[i])
        
    for i in range(len(result2)):
        result2[i] = int(result2[i])
    
    
    matrix = [result1[0:2],result2[0:2]]
    matrix_result = [result1[2],result2[2]]

    resultAll = np.linalg.solve(matrix,matrix_result)
    
    new_w0, new_w1 = resultAll
    
    return new_w0, new_w1

def MA_foresee(b,p):
    SMA_res = 0

    for i in range(p):
        sum_b = len(b) - i -1
        SMA_res += b[sum_b]
        SMA_res /= p
    return SMA_res
# Автокорегресія :
def auto_reg(a,b,p=1):
    w0,w1 = minMNK(a,b)
    function = w0
    #print(w0)
    result_array = []
    for i in range(p):
        len_arr = len(a) - i -1
        
        w0,w1 = minMNK(a[0:len_arr],b[0:len_arr])
        #print('liner - ',res_liner_regr, 'b - ',b[len_arr])
        function += b[len_arr] * w1
        
        result_array.append(function)
    return function
def ARIMA_with_Prediction(step, x,y,p,q,d):
  new_y = [0]
  new_y1 = []
  
  resut_arr = []
  MA_plust_ar = 0
  
  if d == 0:
    new_x = []
    new_y = []
    new_x = x
    new_y = y
    my_x_x = 199
    for i in range(step):
      MA_res = MA_foresee(new_y,q)
      AR_res = auto_reg(new_x,new_y,p=p)
      MA_plust_ar = MA_res + AR_res
      resut_arr.append(MA_plust_ar)
      new_y.append(MA_plust_ar)
      my_x_x +=1
      new_x.append(my_x_x)
    return resut_arr
# data = pd.read_csv("mainData.csv")
# temp_y = []
# temp_y.extend(data['value'])
# y = []
# for i in range(len(temp_y)):
#     temp = temp_y[i]
#     y.append(temp)

# x = []
# for i in range(len(y)):
#     x.append(i)

# print(ARIMA_with_Prediction(2,x,y,p=1,q=7,d=0))
