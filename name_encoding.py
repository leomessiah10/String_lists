print('This program encodes your name into cipher key')

name = input('Enter your name\n:-')
listi = []
number = 0
code = ''

for ch in name:
    num = ord(ch)
    listi.append(num)
    number += num

print(listi)

print('The sum of encoding digits is {}'.format(number))
