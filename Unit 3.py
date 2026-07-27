#Unit 3 The South African Fuel Cost Calculator

kilometers = int(input("How many kilometers they want to drive"))
petrol_price = float(input("What is the current pertrol price per liter"))

liters_needed = kilometers // 10

Total_cost = liters_needed * petrol_price

print(f"The number of liters are {liters_needed} and the total cost is {Total_cost}")

