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
myIndexTest = "I Hate java script"
#Slicing And Indexing
print(myIndexTest[4:9]) # Using slicing and indexing to isolate value elements Note THAT END ELEMENT IS NOT INCLUDED So if you want from 4 to 8 you will type [4:9] 
print(myIndexTest[::3])
#String Methods
print(len(myIndexTest)) # Here you can clearly see we used the len function to print the number of characters of our variable
print(myIndexTest.strip())
print("myIndexTest".title())
print(myIndexTest.capitalize())

e, f, g = "2", "5", "99"
print(e.zfill(2))
print(f.zfill(2))
print(g.zfill(2))

z = "Mango-Is-My-Favourite-Fruit-In-Summer"
print(z.upper())
print(z.split("-", 3))

k = "Korgii"
print(k.center(10, "0")) # Using .center method with parameter of 10 total characters and symbol "0" to center the string in

m = "Can't\tyou\tbe\tso\tgentle\tCan't\tyou\tbe\t??"
print(m.count("Can't", 0, 99)) # Counts 2 Can't words in the string like so nOTE that the 0 is the starting word we need counted so always start with 0 if you give a start and end point :)

print(m.swapcase())

print(m.startswith("C", 23, 38)) # Using start and end points to determine boolean

print(m.endswith("e", 0, 12))

print(k.rjust(10, "O")) # Filling out 4 O's in the word left side because the word is right justified

w = """Korgii
Treason
Mahdy"""
print(w.splitlines())

print(m.expandtabs(9))
#Boolean Methods
kamo = "Brother Oma Opa Geschwester"
print(kamo.isalpha()) #isalpha, identifier, upper, lower, alnum, tite, space ...

print(kamo.replace("Oma", "1", 2)) 

myCampingList= ["Mahdy", "Korgii", "Zema"]

print("-".join(myCampingList))

#Old Formatting And Placeholders
name = "Ian"

price = 200

age = 92

print("Mein name ist: %s und ich koste: %s und ich bin %s jahre ult" % (name, price, age)) 
# Here we clearly used a placeholder to fix the otherwise troubled code because 
# we can concatenate int with string so we do %s and outside quote use % and then () and the replacements in order
print("My name is: %s and i cost: %.2f in the black market and im : %d years old" % (name, price, age)) 
# %s --> String
# %d --> Digit
# %f --> Floating and you can control number of zeroes after . by typing %.5f for example to have 5 zeroes




# n = "Amr"
# l = "Pythonista"
# y = 10

# print("My name is : %s and i have %d years of expierence in %s" % (n, y, l)) 

Obunga = "Korgii"

sen = 17

country =  "Egypt"
print("Hello my name %s and i am %d years old and i currently live in %s" % (Obunga, sen, country))

name2 = "    Elzero     "
print(name2[1])
print(name2[2])
print(name2[5])
