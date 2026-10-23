def main():
    fruits = [
        {"name": "Apple", "calories": 130},
        {"name": "Avocado", "calories": 50},
        {"name": "Banana", "calories": 110},
        {"name": "Cantaloupe", "calories": 50},
        {"name": "Grapefruit", "calories": 60},
        {"name": "Grapes", "calories": 90},
        {"name": "Honeydew Melon", "calories": 50},
        {"name": "Kiwifruit", "calories": 90},
        {"name": "Lemon", "calories": 15},
        {"name": "Lime", "calories": 20},
        {"name": "Nectarine", "calories": 60},
        {"name": "Orange", "calories": 80},
        {"name": "Peach", "calories": 60},
        {"name": "Pear", "calories": 100},
        {"name": "Pineapple", "calories": 50},
        {"name": "Plums", "calories": 70},
        {"name": "Strawberries", "calories": 50},
        {"name": "Sweet Cherries", "calories": 100},
        {"name": "Tangerine", "calories": 50},
        {"name": "Watermelon", "calories": 80},
        {"name": "Mulberry", "calories": 0}
    ]

    request = input("Item: ").strip().capitalize()
    calorie = fruit_search(request, fruits)

    if calorie is None:
        print("Not Available")
    else:
        print(f"Calories: {calorie}")

def fruit_search(req, f):
    for fruit in f:
        if req == fruit["name"]:
            return fruit["calories"]

main()