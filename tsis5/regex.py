import re

#--------FIRST--------#
text = "aaabb"
matches = re.findall(r'a[b]*', text)
print("FIRST")
for match in matches:
    print(match)


#--------SECOND--------#
text = "abbbb abbb ab adsadsadsd abb"
matches = re.findall(r'a[b]{2,3}', text)
print("SECOND")
for match in matches:
    print(match)

#--------THIRD--------#
text = "a_b_c dasdsds saads_dsads_sadsda"
matches = re.findall(r'[a-z]+_[a-z]+', text)
print("THIRD")
for match in matches:
    print(match)

#--------FOURTH--------#
text = "Sdadsdsadsads SSDDSDDSdsdsds dsdsdsds"
matches = re.findall(r'[A-Z][a-z]*', text)
print("FOURTH")
for match in matches:
    print(match)

#--------FIFTH--------#
text = "asddsdsdsb"
text1 = "adssdad"
matches = re.findall(r'a.*b$', text)
print("FIFTH")
for match in matches:
    print(match)

#--------SIXTH--------#
text = "dssddds,sdsda. dsass"
new_text = re.sub(r'[ ,.]', ':' , text)
print("SIXTH")
print(new_text)

#--------SEVENTH--------#
def snake_to_camel(str):
    return re.sub(r'(?!^)_([a-zA-z])', lambda m: m.group(1).upper(), str)

snake_str = 'test_surely_clueless'
camel_str = snake_to_camel(snake_str)
print("SEVENTH")
print(camel_str)

#--------EIGHTH--------#
def mySplit(str):
    return re.findall('[A-Z][^A-Z]*', str)

str = "AsdadssadsaVsdsadsaDdsasadSSDsa"
print("EIGHTH")
print(mySplit(str))

#--------NINTH--------#
def insert_spaces(str):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', str)

str = 'AdsaddsaDdsdsadsDSdsads'
print("NINTH")
print(insert_spaces(str))

#--------TENTH--------#
def camel_to_snake(str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', str).lower()

snake_str = camel_to_snake(camel_str)
print("TENTH")
print(snake_str)