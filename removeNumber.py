str="suneel7351rajput91"
res=""


for i in range(len(str)):
   if (str[i]>='a' and str[i]<='z') or (str[i]>='A' and str[i]<='Z'):
     res=res+str[i]
     
print(res)
