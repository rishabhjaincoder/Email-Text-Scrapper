# Email address text scrapper using regular expressions

import re

text = 'Email addresses of jims students are:- Rishabhjain.rdps@gmail.com jain.naman@jimsindia.org ravneetsingh001@jimsindia.org';

pattern = re.compile('[a-zA-Z0-9\.]+\@[a-zA-Z0-9]+\.[a-zA-Z]+') 

result = pattern.findall(text)

print(result)