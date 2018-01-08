print('This program counts the number in the sentence')

line = input('Enter the sentence\n:-')
count = 0

line_list = line.split()

for i in line_list:
    #print(i)
    count+=1

print(line_list)
print('There are {} words in the sentence'.format(count))
