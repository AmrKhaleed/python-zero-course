#-------------------------------------------------------------------------------------------
#Data Types#
#?type() => Ident Type Of Printed Data
print(type(12)) #int => Integer Data
print(type(12.2)) # float => Floating Point Number or just a decimal value really
print(type("Hello World")) # str => String
print(type([1,  2, 3, 4, 5])) # list => List Inside Square Brackets
print(type((1, 2,  3, 4, 5))) # tuple => Tuple Inside Reg Brackets
print(type({"One": 1, "Two": 2, "Three": 3,})) #dict => Dictionary
print(type(2==2)) #bool => Boolean Does It Make Any Sense ??
# --------------------------------------------------------------------------------------------
#?Variables
name = "My Value" # Normal => One word naming
print(name)
my_Variable = "My Value" # Two Words => Snake Case
myVariable = "My Value" #Two Words => Camel Case
# You can use use multiple values for multiple variables in one line as follows 
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
#---------------------------------------------------------------------------------------------
#? Escape Sequences Characters 
print("Hello\bWorld") # Prints out "HellWorld" removes O letter
print("I love \
python \
Egypt")
print("I Love Egypt So Much \\") # Application of backslash neglects the following backslash so we add another backslash to cancel them both while still remaining in the line of code
print("I love quote marks \"see?\"") # You may also use the opposite of the quotes you are using in the string so in this case just line it in single quotes 
print("I Love Line\nFeed Man")
print("1234567\rabcde")
print("I Hate\tJavascript")
print("\x47\x73") # Types Gs in terminal using the corresponding Hex Numbers
#---------------------------------------------------------------------------------------------
#?Concatenation
msg = "I Love"
lang = "Python"
alpha = 2
bravo = 10
complete = (alpha + bravo)
print(complete)
print(msg + " " + lang) # To space between them we add  a " " and space them accordingly or simply add the space in the variable value  before printing as in  " I Love Python" :)
full = msg + " " + lang # Here we merged 2 variables then just placed them under 1 variable to avoid typing both of them every time they are used which is much better
print(full)
a = "First, Second, Third"
b= "A, B, C"
print(a + "\n" + b) # Here we made a line feed using \n as you can see with the concatenated variables but we had to put the \n in "" to treat as a string because else it wouldn't work 
print("Hello World")  # ERROR Here you can see clearly that you can not in fact concatenate strings with integers
#--------------------------------------------------------------------------------------------
#?Strings
myStringOne = """ Lorem 
Ipsum
Amet"""
#Up here using Triple double quotes or even using triple single quotes does mulitiple lines in one variable
print(myStringOne)
myIndexTest = "   I Hate Java script   "
#Slicing And Indexing
print(myIndexTest[4:9]) # Using slicing and indexing to isolate value elements Note THAT END ELEMENT IS NOT INCLUDED So if you want from 4 to 8 you will type [4:9] 
print(myIndexTest[::3])
#String Methods
print(len(myIndexTest)) # Here you can clearly see we used the len function to print the number of characters of our variable
print(myIndexTest.strip())
print(myIndexTest.title())
print(myIndexTest.capitalize)

e, f, g = "2", "5", "99"
print(e.zfill(2))
print(f.zfill(2))
print(g.zfill(2))

z = "Mango-Is-My-Favourite-Fruit-In-Summer"
print(z.upper())
print(z.split("-", 3))

k = "Korgii"
print(k.center(10, "0")) # Using .center method with parameter of 10 total characters and symbol "0" to center the string in

m = "Can't you be so gentle Can't you be ??"
print(m.count("Can't", 0, 99)) # Counts 2 Can't words in the string like so nOTE that the 0 is the starting word we need counted so always start with 0 if you give a start and end point :)

print(m.swapcase())

print(m.startswith("C", 23, 38)) # Using start and end points to determine boolean

print(m.endswith("e", 0, 12))