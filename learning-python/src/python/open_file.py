fileName = raw_input("Please enter the file to open: ");
fhand = open(fileName)
for line in fhand:
    print line