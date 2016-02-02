dictionary = dict()
dictionary['name'] = 'mohanraj'
dictionary ['surname'] = 'pant'
dictionary['house_no'] = 808
dictionary['post_code'] = 'TW7 5NA'
dictionary['city'] = 'London'
dictionary['country'] = 'United Kingdom'
dictionary['mobile_no'] = '07449300335'

print dictionary.keys()

print dictionary.values()

print dictionary.items()

print list(dictionary)

for key in dictionary:
    print dictionary[key]

for key, value in dictionary.items():
    print key,  '--> ', value