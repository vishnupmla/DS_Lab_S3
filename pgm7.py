print('---------Tuples operations---------')
d = {(x, x+1): x for x in range(10)}
print('Dictionary with tuple keys')
for inx, val in d.items():
    print('{} : {}'.format(inx, val))

t = (5, 6)
print('\nTuple t: ', t)
print('d[t] implies: ', d[t])
print('d[1,2] implies: ', d[1, 2])
