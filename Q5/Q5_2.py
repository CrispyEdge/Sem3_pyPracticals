dic1 = {1: "OK", 2: "YES", 3: "WHat?"}
dic2={3:30,4:40}

dic4 ={}

for d in (dic1, dic2):
    dic4.update(d)
    
print(dic4)