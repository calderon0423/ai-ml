# Collect the user's input for the prompt "What is your name?"
user_name = input("What is your name? ")

# Print the data type of user_name
print("user_name is type", type(user_name))

# Collect the user's input for the prompt "How old are you?" and convert the
# string to an integer.
age = int(input("How old are you? "))

# Print the data type of age
print("age is type", type(age))

# Collect the user's input for the prompt "What is your average weekly grocery 
# bill?" and convert the string to a float.
avg_wkly_bill = float(input("what is your weekly average grocery bill? "))

# Print the data type of grocery_bill
print("avg_wkly_bill is type", type(avg_wkly_bill))

# Collect the user's input for the prompt "Will you type an input?" and
# convert it to a boolean. Note that non-zero, non-empty objects return True.
input_ = bool(input("Will you type an input? "))

# Print the data type of true_or_false
print("Input is type", type(input_))

# Create four print statements that displays text about the user's inputs
print("The user's name is",user_name)
print("The user's age is", age)
print("Their weekly average grocery bill is",avg_wkly_bill)
print("Will the user require an input?",input_)
