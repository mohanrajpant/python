number = [10, 7, 6, 5, 2, 11, 34, 1, 4]
smallest = None
for value in number:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
print 'The smallest number is', smallest

for val in range(1, 10):
    print(val)


