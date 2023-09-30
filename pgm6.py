print("------Set operations------")
set1 = {66, 100, 110}
print('Set \'set1\' contain elements: ', set1)
set1.add(120)
print('After inserting \'120\' to \'set1\': ', set1)
set1.update([50, 60, 70])
print('After inserting mutliple values to \'set1\': ', set1)
set1.remove(60)
print('After deleting \'60\' from \'set1\': ', set1)

print('\nSet comprehension and set operations:')
set2 = {i for i in range(10)}
set3 = {i for i in range(10) if i % 2 != 0}
print('Values in \'set2\' are: {} \nValues in \'set3\' are: {}'.format(set2, set3))
print('\nUnion operation (set2 U set3): ', set2 | set3)
print('Intersection operation (set2 & set3): ', set2 & set3)
print('Difference (set2 - set3): ', set2-set3)
