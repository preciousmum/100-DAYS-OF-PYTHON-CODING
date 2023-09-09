# Creating functions with outputs

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return (f"{formated_f_name} {formated_l_name}")

# formated_string = format_name("negedu","jeremiah")
# print(formated_string)
print(format_name("negedu", "jeremiah"))

# when you use return keyword it doesn't do anything after it, i.e it stops there
#  The return eyword simply ends thecode where it is

# Multiple return statement
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return (f"{formated_f_name} {formated_l_name}")
print(format_name(input("What is your first name? "), input("What is your last name? ")))

