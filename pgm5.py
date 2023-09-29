print('--------Dictionary Operations----------')
d = dict()
d={'cat':'cute','dog':'furry'}
print("Dictionary: ",d)
print("Is the dictioanry has the key \'cat'?\n",'cat' in d)

d['fish']='wet'
print('After adding new entry to \"d" ',d)
print("Get an element \'Monkey': ",d.get('monkey','Not found'))
print("Get an element \"fish\" : ",d.get('fish','Not found'))

del d['fish']
print('After deleting element Fish from dictionary "d": ',d)
print('\nDemo of Dictionary comprehension')
sqrs = {x:x*x for x in range(10)}
print("Squares of integers of range 10: ")
for k,v in sqrs.items():
    print("{} : {}".format(k,v))