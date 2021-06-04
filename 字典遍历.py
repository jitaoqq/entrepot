dict = {"k1":"v1","k2":"v2","k3":"v3"}
key = dict.keys()
value =dict.values()
for ke in key:
    print(ke)
for va in value:
    print(va)

dict["k4"]="v4"
print(dict)