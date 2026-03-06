import json

# Task 1: Read inventory
with open("inventory.json", "r") as file:
    inventory = json.load(file)

print("Total books in inventory:", len(inventory))

# New book to add
new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True
}

# Add the new book
inventory.append(new_book)

# Write updated inventory back to file
with open("inventory.json", "w") as file:
    json.dump(inventory, file, indent=4)

# Read updated inventory
with open("inventory.json", "r") as file:
    updated_inventory = json.load(file)

# Display each book
for book in updated_inventory:
    print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']}")    