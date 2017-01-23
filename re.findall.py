import re
x= 'My 2 favorate numbers are 19 and 42'
y=re.findall('[aeiou]+',x)
print (y)


import re
x= 'From: Using the : character'
y=re.findall('^F.+:',x)
print (y)


import re
x= 'From: Using the : character'
y=re.findall('^F.+?:',x)
print (y)
