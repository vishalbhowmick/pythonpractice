import random
x = int(input('password length\n'))
s = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
y = ''.join(random.sample(s,x))
print(y)
