import re
def read_return_arr():
    arr_list = []
    temp = [] 
    with open("dht22.txt","r") as f:
        temp = f.read()
        temp = re.findall(r'\d+\.\d+', temp) 
            
    normal_temp = []
    for i in range(len(temp)):
        normal_temp.append(float(temp[i]))
    return normal_temp

temp  = read_return_arr()
print(type(temp[]))
