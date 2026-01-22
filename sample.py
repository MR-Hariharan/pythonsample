#Creating dictionary using dict
my_cat = {"number": 120, " details":{"color":"white","bread":"ooty"}}
print(my_cat)
print(my_cat["number"])
print(my_cat["details"]["color"])
print(my_cat["details"].get("color"))
print(my_cat.get("details").get("color"))
