print('This program evaluates the grade of the student')

marks = eval(input('Enter your marks between 70 to 100 !!'))

li_1 = [90,91,92,93,94,95,96,97,98,99,100]
li_2 = [80,81,82,83,84,85,86,87,88,89]
li_3 = [70,71,72,73,74,75,76,77,78,79]



if marks in li_1:
    print('A')

elif marks in li_2:
    print('B')

elif marks in li_3:
    print('C')

else:
    print('You are avreage below student')


