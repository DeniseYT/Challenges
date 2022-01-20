# Python programmers write variable names in snake_case, where each word is lowercased and joined by underscores. JavaScript programmers write variable names in camelCase, where the initial word is lowercase, and other words are capitalized and jammed together.

# Given a variable name in snake_case, return a string with that variable name written in camelCase.

# For example:
# >>> snake_to_camel("hi_balloonicorn")
# 'hiBalloonicorn'


# Start my solution:

# My solution 1
def snake_to_camel(variable_name):

    new_string = ""

    new_name = variable_name.split("_") #seperate words by "_" and convert to a list
    # print(new_name) #['hi', 'balloonicorn', 'yes']
    
    for i in range(1, len(new_name)):
        x = new_name[i].capitalize()
        # print(x) #Balloonicorn #Yes
        new_string += x
        # print(new_string)

    return new_name[0] + new_string
        
print(snake_to_camel("hi_balloonicorn_yes")) 


# My solution 2
def snake_to_camel(variable_name):

    new_name = variable_name.split("_")

    for i in range(1, len(new_name)):
        new_name[i] = new_name[i].capitalize()
        # print(new_name[i]) #Balloonicorn #Yes

    return "".join(new_name) #convert list to string

print(snake_to_camel("hi_balloonicorn_yes")) 
