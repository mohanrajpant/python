file = raw_input("Please enter the file name for which you want to count the line: ")
fhand = open(file)
# count = 0
# for line in fhand:
#     count +=1
# print 'The total no of line in file is: ', count

count2 = fhand.read()

# print 'The total no of line in file is: ', len(count2)
print count2[:25]