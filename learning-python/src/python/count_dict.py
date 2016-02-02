counts = dict()
names = ['mohanraj', 'Deepakraj', 'Ahaan', 'Deepakraj', 'Ahaan', 'Ahaan']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print counts

# if exist get else o

print counts.get('Leela', 0)
print counts.get('Ahaan', 5)

for key in counts:
    print key, counts[key]

for data in counts:
    print data, counts[data]