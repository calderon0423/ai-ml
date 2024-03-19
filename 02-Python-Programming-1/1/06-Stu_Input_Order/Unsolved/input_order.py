# Take input of an item the user wants to purchase
purchase_item = input("What item would you like to purchase? ")

# Ask how much the item costs and cast it as a number.
# What type of number should it be cast as?
item_cost = float(input("How much does the item cost? "))


# Ask what quantity of the item should be purchased and cast it as a number.
# What type of number should it be cast as?
item_quantity = int(input("How many units do you want to purchase? "))


# Print the item cost along with its data type
print("The item costs is",item_cost)
print("item_cost is data type",type(item_cost))
# Print the item quantity along with its data type
print("The item quantity is",item_quantity)
print("item_quantity is data type",type(item_quantity))

# Print results
print("The total cost for the",purchase_item,"is",item_cost*item_quantity)
print(f"The total cost of the {purchase_item} is {item_cost*item_quantity:10.2f}\n")
