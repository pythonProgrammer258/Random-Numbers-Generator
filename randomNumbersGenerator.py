# Random numbers generator
# 2022 pythonProgrammer258
# Open source license

import random
import string
numbers = string.digits
repeats = string.digits

n1 = random.choice(numbers)
n2 = random.choice(numbers)
n3 = random.choice(numbers)
n4 = random.choice(numbers)
n5 = random.choice(numbers)
n6 = random.choice(numbers)
n7 = random.choice(numbers)
n8 = random.choice(numbers)
n9 = random.choice(numbers)

repeat = random.choice(repeats)

print('Random number generator')
if repeat == '1':
    print(f'{n1}')
elif repeat == '2':
    print(f'{n1}{n2}')
elif repeat == '3':
    print(f'{n1}{n2}{n3}')
elif repeat == '4':
    print(f'{n1}{n2}{n3}{n4}')
elif repeat == '5':
    print(f'{n1}{n2}{n3}{n4}{n5}')
elif repeat == '6':
    print(f'{n1}{n2}{n3}{n4}{n5}{n6}')
elif repeat == '7':
    print(f'{n1}{n2}{n3}{n4}{n5}{n6}{n7}')
elif repeat == '8':
    print(f'{n1}{n2}{n3}{n4}{n5}{n6}{n7}{n8}')
elif repeat == '9':
    print(f'{n1}{n2}{n3}{n4}{n5}{n6}{n7}{n8}{n9}')
