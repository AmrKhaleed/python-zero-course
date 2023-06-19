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
print("I love quote marks \"see?\"")
print("I Love Line\nFeed Man")
print("1234567\rabcde")
print("I Hate\tJavascript")
print("\x47\x73") # Types Gs in terminal using the corresponding Hex Numbers
#---------------------------------------------------------------------------------------------
#?Concatenation
msg = "I Love"
lang = "Python"

print(msg + " " + lang) # To space between them we add  a " " and space them accordingly or simply add the space in the variable value  before printing as in  " I Love Python" :)
full = msg + " " + lang # Here we merged 2 variables then just placed them under 1 variable to avoid typing both of them every time they are used which is much better
print(full)
a = "First, Second, Third"
b= "A, B, C"
print(a + "\n" + b) # Here we made a line feed using \n as you can see with the concatenated variables but we had to put the \n in "" to treat as a string because else it wouldn't work 
print("Hello World")  # ERROR Here you can see clearly that you can not in fact concatenate strings with integers