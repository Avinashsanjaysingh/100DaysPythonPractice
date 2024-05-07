
# Strings are immutable
a = "!!!Avinash!! !!!!!!!!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())

b = " Silver Spoon "
print(b.strip())
print(a.rstrip("!"))
print(a.replace("Avinash", "John"))
print(a.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(str1.center(50 ))
print(len(str1))
print(len(str1.center(50)))
print(a.count("Avinash"),'\n')

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome  to the Console !!!"
print(str1.endswith("to", 4, 10),'\n')       

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))    # find method returns the index of the first found string.
print(str1.find("is")) # find method returns '-1' in case of no match.
print(str1.index("is"),'\n')
# print(str1.index("is"))   # this throw an error

str1 = "WelcomeToTheConsole"
print(str1.isalnum())   # isalnum (a-z,A-Z,0-9)(no spaces & symbols)
str1 = "Welcome "
print(str1.isalpha())   # isalpha (only a-z,A-Z)

str1 = "hello world 2"
print(str1.islower(),'\n')  # only checks for availability of capital if present returns false

str1 = "We wish you a Merry Christmas"
print(str1.isprintable())   # will return false when non-printable are present like (\n )
str1 = "         "       #using Spacebar
print(str1.isspace())   # returns true only when white space is present 
str2 = "  "       #using Tab
print(str2.isspace(),'\n')

str1 = "World Health Organization" 
print(str1.istitle())   # returns true only when first character of each strings are capital

str2 = "To Kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))    # startswith is opposite of endswith # It checks the starting characters of the string   # it is case sensitive

str1 = "Python is a Interpreted Language" 
print(str1.swapcase()) # it changes cases from lower to upper & from upper to lower

str1 = "His name is Dan. Dan is an honest man."
print(str1.title()) # it changes 1st character of each string to capital

