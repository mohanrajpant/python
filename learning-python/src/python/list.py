def print_stuff(stuff) :
    for val in stuff:
        print 'Hi Welcome to London', val

stuff = list()
stuff.append('mohanraj')
stuff.append('soni')
stuff.append('tukku')

stuff.append('deepak')

print 'Before sorting'
print_stuff(stuff)

stuff.sort()
print 'After sorting'
print_stuff(stuff)

if 'soni' in stuff:
    print 'love you soni'
