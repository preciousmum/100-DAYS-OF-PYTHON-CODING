Programming_dictionary = {
    "Bug": "An error in a program that prevents the program form running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# #Retrieving item in a dictionary
print(Programming_dictionary["Function"])

# #Adding items to a dictionary
Programming_dictionary["Loop"] = "The action of doing something over and over again"
print(Programming_dictionary)

# #Creating an empty dictionary 
empty_dictionary = {}


# # wiping a dictionary
Programming_dictionary = {}

# #Editing or adding an item in a dictionary
Programming_dictionary["Bug"] = "A moth in your computer"
print(Programming_dictionary)

#Loop through a dictionary
for key in Programming_dictionary:
    # prints only the key
    print(key)
    # To print value you use the code below
    print(Programming_dictionary[key])

# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting a Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits":12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 4}
}

# Nesting a dictionary inside a list 
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_vists": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_vists": 5
    }
]
