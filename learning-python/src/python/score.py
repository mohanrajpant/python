try:
    score = raw_input('Enter score between 0.0 to 1.0:')
    i_score = float(score)
    if (i_score < 0.0) or (i_score > 1.0):
        raise Exception('out of range')
except:
    print 'Please, enter numeric number between'
    quit()

if i_score >= 0.9:
    print 'A'
elif i_score >= 0.8:
    print 'B'
elif i_score >= 0.7:
    print 'C'
elif i_score >= 0.6:
    print 'D'
else:
    print 'F'
