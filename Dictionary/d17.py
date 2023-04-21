d1={"lol":10,"mano":20,"aoi":25,"jo":25}
lol=0
for k,v in d1.items():
    print("names = ",k,"values = ",v)
    v=lol+v
    lol=v
print("Total = ",lol)