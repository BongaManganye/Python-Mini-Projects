# Automated Invoice Generator

customer = input("Enter customer name: ")
items = []
while True:
    item = input("Enter item (or 'done to finish): ")
    if item.lower() == "done":
        break
    price = float(input("Enter price: "))
    items.append((item, price))

total = sum(price for _, price in items)

invoice = f"Invoice for {customer}\n " + "-" * 30 + "\n"
for item, price in items:
    invoice += f"{items}: \${price:.2f}\n"
invoice += f"Total: \${total:.2f}\n"

with open("invoice.txt", "w") as file:
    file.write(invoice)

print("Invoice saved to invoice.txt")
