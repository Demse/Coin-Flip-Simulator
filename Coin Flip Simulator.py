import random
print('Welcome to a coin flip simulator')
count = 0
Heads = 0    
Tails = 0



trials = int(input('How many number of flips: '))


while count < trials:
    
    result = random.randint(1,2)
    if result == 1:
        Heads +=1
    elif result == 2:
        Tails += 1
    count += 1
print(f' no. of Heads: {Heads}')
print(f' no. of Tails: {Tails}')
print(f'Heads: {Heads/trials}%')
print(f'Tails: {Tails/trials}%')
