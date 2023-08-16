Programming_dictionary = {
    "Bug": "An error in a program that prevents the program form running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving item in a dictionary
print(Programming_dictionary["Function"])

#Adding items to a dictionary
Programming_dictionary["Loop"] = "The action of doing something over and over again"
print(Programming_dictionary)

#Create an empty dictionary 
empty_dictionary = {}


# wiping a dictionary
Programming_dictionary = {}

#Editing an item in a dictionary
Programming_dictionary["Bug"] = "A moth in your computer"
print(Programming_dictionary)

#Loop through a dictionary
for key in Programming_dictionary:
    print(key)
    # To print value you use the code below
    print(Programming_dictionary[key])