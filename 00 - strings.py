# multiple ways to write a string

# using single Quote
message1 = 'Hi this is from Python'
print('message 1 : ' + message1)

# using double quote
message2 = "Hi this is from Python"
print('message 2 : ' + message2)

# using double qoute and single quote
message3 = '''Hi this is from Python and I'm pretty sure what they say about python. "This is a nice language" as they said.'''
print('message 3 : ' + message3)

# concatenation
concatenatedmessage = 'This is concate' + 'nated example.'
print('This is concate + nated example. : ' + concatenatedmessage)

# splitting
myname = 'aritra mukherjee'
print('My first name is : '+ myname.split(' ')[0]) # aritra
print('My last name is : ' + myname.split(' ')[1]) # mukherjee

# print length
# print('My name is : ' + myname + ' and it has ' + myname.count() + ' characters.')

################################################
#various functions who returns boolean##########
################################################

# isalnum
print('myname is alnum() :' , myname.isalnum())

# isalpha
print('myname is isalpha() :' , myname.isalpha())

# isdecimal
print('myname is isdecimal() :' , myname.isdecimal())

# isdigit
print('myname is isdigit() :' , myname.isdigit())

# isidentifier
print('myname is isidentifier() :' , myname.isidentifier())

# islower
print('myname is islower() :' , myname.islower())

# isnumeric
print('myname is isnumeric() :' , myname.isnumeric())

# isprintable
print('myname is isprintable() :' , myname.isprintable())

# isspace
print('myname is isspace() :' , myname.isspace())

# istitle
print('myname is in title format :' , myname.istitle())

# isupper
print('myname is isupper() :' , myname.isupper())

################################################
#various functions who returns string###########
################################################
# capitalize
print('myname after capitalize() :' , myname.capitalize())

# startswith
print('myname startswith("ari") :' , myname.startswith("ari"))

# endswith
print('myname endswith("jee") :' , myname.endswith("jee"))

# swapcase
print('myname after swapcase() :' , myname.swapcase())

# lower
print('myname after lower() :' , myname.lower())

# upper
print('myname after upper() :' , myname.upper())

# replace
print('myname after replace(aritra, iatim) :' , myname.replace('aritra', 'iatim'))

# title
print('myname after title() :' , myname.title())

# index, rindex
# if string not found returns error
print('myname after index("t") :' , myname.index('t'))
print('myname after rindex("j") :' , myname.rindex('j'))

# find, rfind
# if string not found returns -1
print('myname after find("t") :' , myname.find('tt'))
print('myname after rfind("j") :' , myname.rfind('jj'))

# # format
# print('myname after format() :' , myname.format())

# # format_map
# print('myname after format_map() :' , myname.format_map())

# # join
# print('myname after join() :' , myname.join())

# # ljust
# print('myname after ljust() :' , myname.ljust())

# # rjust
# print('myname after rjust() :' , myname.rjust())

# # strip
# print('myname after strip() :' , myname.strip())

# # lstrip
# print('myname after lstrip() :' , myname.lstrip())

# # rstrip
# print('myname after rstrip() :' , myname.rstrip())

# # partition
# print('myname after partition() :' , myname.partition())

# # rpartition
# print('myname after rpartition() :' , myname.rpartition())

# # maketrans
# print('myname after maketrans() :' , myname.maketrans())

# # splitlines
# print('myname after splitlines() :' , myname.splitlines())

# # casefold
# print('myname after casefold() :' , myname.casefold())

# # center
# print('myname after center() :' , myname.center())

# # count
# print('myname after count() :' , myname.count())

# # encode
# print('myname after encode() :' , myname.encode())

# # translate
# print('myname after translate() :' , myname.translate())

# # zfill
# print('myname after zfill() :' , myname.zfill())

# # expandtabs
# print('myname after expandtabs() :' , myname.expandtabs())