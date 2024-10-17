acc = 0
pos = 0 
neg = 0
count = 0
x = int(input('Enter an integer, the input ends if it is 0: '))
if x == 0:
    print('No numbers are entered except 0')
else:
    while x != 0:
        count += 1
        acc += x
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        x = int(input('Enter an integer, the input ends if it is 0: '))
    print('The number of positives is: ',pos)
    print('The number of negatives is: ',neg)
    print('The total is:',acc)
    print(f'The average is: {acc/count:.2f}')