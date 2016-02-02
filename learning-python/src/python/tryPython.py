sAge = raw_input('Enter you age:')
try:
    # print 'Hello'
    iAge = int(sAge)
    # print 'There'
except:
    iAge = -1

if iAge > 0:
    print 'Nice Work'
else:
    print 'Not a Number'

