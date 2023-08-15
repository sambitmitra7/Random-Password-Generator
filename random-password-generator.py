import random
import string

print('Random Password Generator')

length = int(input('Enter desired password length: '))  

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

password = ''.join(random.sample(all,length)) 

print(password)
