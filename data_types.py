#String data type

#literal assignment
first = "Dave"
last = "Gray"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

#constructor function

# pizza = str("Pepperoni")

# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

#Concatenation
# fullname = first + " " + last
# print(fullname)

# fullname += '!'
# print(fullname)

#Casting a number to a string

# decade = str(1980)
# print(type(decade))
# print(decade)

# statement = "I like rock usic from the " + decade + "s."
# print(statement)

# #multiple lines
multiline = '''
Hey, how are you?
I was just checking in.
                            All good?
'''
# print(multiline)

#Escaping special characters
# sentence = 'I\'m back at work! \tHey!\n\nWhere\'s this as\\located?'
# print(sentence)

#String methods
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())
# print(multiline.replace("good", "ok"))

# print(len(multiline))
# multiline += "                                      "
# print(len(multiline))
# multiline = "                           " + multiline
# print(len(multiline))
# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))

#Building a menu

title = "Menu".upper()
# print(title.center(20, "="))
# print("Cofee".ljust(16, ".") + "$1".rjust(4))
# print("Muffin".ljust(16, ".") + "$2".rjust(4))
# print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

# print("")

# #String index values
# print(first[0:])

#Boolean data methods

# print(first.startswith("D"))
# print(first.endswith("Z"))

#Booleans
myval = True
x = bool(False)

# print(type(x))
# print(isinstance(myval, bool))

#I'm skipping the next few because I already know all of this stuff