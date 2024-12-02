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
    1: [""],
    2: ["", ""],
    3: ["", "", ""],
    4: ["", "", "", ""],
    5: ["", "", "", "", ""],
    6: ["", "", "", "", "", ""],
    7: ["", "", "", "", "", "", ""],
    8: ["", "", "", "", "", "", "", ""]
}

print("\nHanukkah Gifts:")
for night, gifts in hanukkahlist.items():
    print(f"Night {night}:")
    for gift in gifts:
        print(f"  - {gift}")