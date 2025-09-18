# Python program for online food  ordering system 
print(" Welcome!")
print("We serve delicious Veg, Non-Veg meals, Biryani, Beverages & Desserts!")
print("Please enter your order as shown in the menu below.\n")

print("""🌿 Veg Starters

Gobi Manchurian (Dry)  – ₹120
Paneer 65              – ₹150
Veg Spring Roll        – ₹130
Mushroom Chilli        – ₹140

🍗 Non-Veg Starters

Chicken 65             – ₹160
Chilli Chicken         – ₹170
Fish Fry               – ₹180
Mutton Pepper Fry      – ₹220

🍛 South Indian Meals

Idli (2 pcs)           – ₹40
Vada (2 pcs)           – ₹50
Dosa (Plain)           – ₹60
Masala Dosa            – ₹80
Onion Rava Dosa        – ₹100
Pongal                 – ₹70
Upma                   – ₹60
Poori (2 pcs)          – ₹70
Full Meals (Unlimited) – ₹150

🍲 Curries (Veg)

Paneer Butter Masala   – ₹160
Veg Korma              – ₹140
Mushroom Curry         – ₹150
Dal Fry                – ₹120

🍲 Curries (Non-Veg)

Chicken Curry         – ₹180
Butter Chicken        – ₹220
Mutton Curry          – ₹250
Fish Curry            – ₹200

🍚 Rice & Biryani

Veg Fried Rice        – ₹130
Veg Biryani           – ₹150
Chicken Fried Rice    – ₹160
Chicken Biryani       – ₹200
Mutton Biryani        – ₹250
Egg Biryani           – ₹160
Curd Rice             – ₹100
Lemon Rice            – ₹90
Tomato Rice           – ₹100

🥤 Beverages

Filter Coffee         – ₹30
Tea                   – ₹20
Badam Milk            – ₹50
Fresh Lime Soda       – ₹40
Soft Drinks           – ₹40

🍨 Desserts

Gulab Jamun (2 pcs)   – ₹60
Ice Cream (2 scoops)  – ₹80
Fruit Salad           – ₹90
Payasam               – ₹70
""")

order = [item.strip().lower() for item in input("Enter your order: ").split(",")]
quantity = list(map(int, input("Enter quantity: ").split(",")))

total = 0

for i in range(len(order)):
    if order[i] == "gobi manchurian (dry)":
        total += 120 * quantity[i]
    elif order[i] == "paneer 65":
        total += 150 * quantity[i]
    elif order[i] == "veg spring roll":
        total += 130 * quantity[i]
    elif order[i] == "mushroom chilli":
        total += 140 * quantity[i]
    elif order[i] == "chicken 65":
        total += 160 * quantity[i]
    elif order[i] == "chilli chicken":
        total += 170 * quantity[i]
    elif order[i] == "fish fry":
        total += 180 * quantity[i]
    elif order[i] == "mutton pepper fry":
        total += 220 * quantity[i]
    elif order[i] == "idli (2 pcs)":
        total += 40 * quantity[i]
    elif order[i] == "vada (2 pcs)":
        total += 50 * quantity[i]
    elif order[i] == "dosa (plain)":
        total += 60 * quantity[i]
    elif order[i] == "masala dosa":
        total += 80 * quantity[i]
    elif order[i] == "onion rava dosa":
        total += 100 * quantity[i]
    elif order[i] == "pongal":
        total += 70 * quantity[i]
    elif order[i] == "upma":
        total += 60 * quantity[i]
    elif order[i] == "poori (2 pcs)":
        total += 70 * quantity[i]
    elif order[i] == "full meals (unlimited)":
        total += 150 * quantity[i]
    elif order[i] == "paneer butter masala":
        total += 160 * quantity[i]
    elif order[i] == "veg korma":
        total += 140 * quantity[i]
    elif order[i] == "mushroom curry":
        total += 150 * quantity[i]
    elif order[i] == "dal fry":
        total += 120 * quantity[i]
    elif order[i] == "chicken curry":
        total += 180 * quantity[i]
    elif order[i] == "butter chicken":
        total += 220 * quantity[i]
    elif order[i] == "mutton curry":
        total += 250 * quantity[i]
    elif order[i] == "fish curry":
        total += 200 * quantity[i]
    elif order[i] == "veg fried rice":
        total += 130 * quantity[i]
    elif order[i] == "veg biryani":
        total += 150 * quantity[i]
    elif order[i] == "chicken fried rice":
        total += 160 * quantity[i]
    elif order[i] == "chicken biryani":
        total += 200 * quantity[i]
    elif order[i] == "mutton biryani":
        total += 250 * quantity[i]
    elif order[i] == "egg biryani":
        total += 160 * quantity[i]
    elif order[i] == "curd rice":
        total += 100 * quantity[i]
    elif order[i] == "lemon rice":
        total += 90 * quantity[i]
    elif order[i] == "tomato rice":
        total += 100 * quantity[i]
    elif order[i] == "filter coffee":
        total += 30 * quantity[i]
    elif order[i] == "tea":
        total += 20 * quantity[i]
    elif order[i] == "badam milk":
        total += 50 * quantity[i]
    elif order[i] == "fresh lime soda":
        total += 40 * quantity[i]
    elif order[i] == "soft drinks":
        total += 40 * quantity[i]
    elif order[i] == "gulab jamun (2 pcs)":
        total += 60 * quantity[i]
    elif order[i] == "ice cream (2 scoops)":
        total += 80 * quantity[i]
    elif order[i] == "fruit salad":
        total += 90 * quantity[i]
    elif order[i] == "payasam":
        total += 70 * quantity[i]
    else:
        print(f"'{order[i]}' is not on the menu!")

print(f"\nTotal Bill = ₹{total}")
