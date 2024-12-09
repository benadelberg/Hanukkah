foodlist = {
    "turkey": 1,
    "cranberry sauce": 3,
    "mashed potatoes": 3,
    "corn": 4,
    "macaroni and cheese": 1,
    "apple pie": 1,
}

print("Food items")
for food, num in foodlist.items():
    print(f"We need {num} {food}")




hanukkahlist = {
    1: ["TV"],
    2: ["Smartwatch", "VR headset"],
    3: ["Car", "Laptop", "Shirts"],
    4: ["Switch", "Turntable", "PC", "Gaming chair"],
    5: ["PlayStation 5", "Smartphone", "Headphones", "Books", "Speakers"],
    6: ["Xbox Series X", "Shoes", "E-Reader", "Drum set", "Camera", ""],
    7: ["", "", "", "", "", "", ""],
    8: ["", "", "", "", "", "", "", ""]
}

print("\nHanukkah Gifts:")
for night, gifts in hanukkahlist.items():
    print(f"Night {night}:")
    for gift in gifts:
        print(f"  - {gift}")