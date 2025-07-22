dict={'codingal':2,"is":2,"the":2,'best':1}
k=2
res =0
for  key in dict:
    if dict[key]==k:
        res=res+1
print(f"the frequency is {str(res)}")