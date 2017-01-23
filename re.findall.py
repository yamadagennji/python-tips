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


x='From stephen.marquard@uct.ac.za Sat Jan 5 09:13:16 2008'
import re
y=re.findall('\S+@\S+',x)
print (y)

x='From stephen.marquard@uct.ac.za Sat Jan 5 09:13:16 2008'
import re
y=re.findall('^From (\S+@\S+)',x)
print (y)

x='From 222 stephen.marquard@uct.ac.za Sat Jan 5 09:13:16 2008'
import re
y=re.findall('^From.* (\S+@\S+)',x)
print (y)

#当需要字符而不是通配符输入时前面加 "\"
