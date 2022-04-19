def f(**kw):
    ke = list(kw.keys())
    for i in range(len(ke)):
        print(kw[ke[i]])


f(brand="Ford",
  model="Mustang",
  year=1964)


# or


def f(dic):
    k = list(dic.keys())
    for i in range(len(k)):
        print(dic[k[i]])


f({'brand': 'Ford', 'model': 'Mustang', 'year': 1964})
