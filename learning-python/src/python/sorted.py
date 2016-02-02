d = {'a': 5, 'c': 10, 'e': 40, 'd': 21, 'b': 22, 'f': 21}
list = d.items()
print list
list.sort()
print list
list.sort(reverse=True)
print list

print sorted(list)

for k, v in sorted(d.items()):
    print k, v