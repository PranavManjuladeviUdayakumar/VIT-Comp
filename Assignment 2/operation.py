#Perform mathematical operations
a = 5
b = 3

for i in '+-*/%':
    print(eval(f'{a} {i} {b}'))
else:
    print(eval(f'{a} ** {b}'))
    print(eval(f"{a} // {b}"))