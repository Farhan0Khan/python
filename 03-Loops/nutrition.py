def main():
    # data of fruits
    fruits = [
        {"name":"apple","calories":"130"},
        {"name":"strawberry","calories":"150"},
        {"name":"banana","calories":"40"},
        {"name":"mango","calories":"150"},
    ]
    # ask user for fruits
    frt = input("Fruit: ")
    check_calorie(frt, fruits)

def check_calorie(frt, fruits):
    for i in fruits:
        if i["name"] == frt:
            print("Calorie:",i["calories"])
        else:
            print("Not available")

main()
