def f(**kw):
    ke=list(kw.keys())
    for i in range(len(ke)):
        print(kw[ke[i]])
    
    
    
    
f(brand= "Ford",
  model= "Mustang",
  year= 1964)
