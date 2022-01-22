lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""

# Now let's create a price for the loveseat.
lovely_loveseat_price = 254.00

stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""

# Now let's assign a price to the stylish settee.
stylish_settee_price = 180.50

luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""

# Now let's assing the luxurious lamp a price.
luxurious_lamp_price = 52.12

# Let's also store tax as a variable.
sales_tax = .088

# Our first customer is making their purchase! 

customer_one_total = 0
customer_one_itemization = ""

# Our customer has decided to buy the Lovely Loveseat. Here we will add the price of the Lovely Loveseat to the previous total of 0.
customer_one_total += lovely_loveseat_price

customer_one_itemization += lovely_loveseat_description

# The customer has also decided to buy the Luxurious Lamp. Here we'll add this to the total.
customer_one_total += luxurious_lamp_price

customer_one_itemization += luxurious_lamp_description

# They're ready to check out. Before they go we need to calculate sales tax.
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

# Now let's start printing out their receipt.
print("Customer One Items:")
print(customer_one_itemization)
print("")
print("Customer One Total:")
print(customer_one_total)