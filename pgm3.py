print('String DataType')
s1 = 'hello'
s2 = 'world'
print('First string = {} \nSecond String = {}'.format(s1,s2))
new = s1+' '+s2
print('Strings after concatenation = ',new)
print('String after capitalizing = ',new.capitalize())
print('String Uppercase = ',new.upper())
print('String after right Justify = ',new.rjust(7))
print('String at center = ',new.center(7))
print('After replacing \"l" with \"ell" = ',new.replace('l','ell'))
print("String after striping leading and trailing white space: ",new.strip())