fname = raw_input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
count = 0
fh = open(fname)
for line in fh :
    if not line.startswith('From'): continue
    details = line.split()
    email_address = details[1]
    count +=1
    print email_address
print 'There were', count, 'lines in the file with From as the first word'