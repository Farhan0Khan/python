def main():
    grocery_list = (get_items())
    sorted_list = sorted(grocery_list)

    if has_duplicates(sorted_list):
        for i in grocery_list:
            seen = []
            


    grocery_dict = []
    for i in sorted_list:
        grocery_dict.append({
            "item_name":i
        })


    for n , i in enumerate(grocery_dict):
        print(f"{n} | {grocery_dict[n]["item_name"]}")
        

def has_duplicates(tup):
    seen = []
    for i in tup:
        if i in seen:
            return True
            seen.append(i)
        return False

    
def get_items():

    items = []

    while True:

        try:
            item = str(input('Item: ').strip().upper())

            if item.isdigit():
                raise ValueError()

            items.append(item)

        except ValueError:
            pass
        except EOFError:
            print()
            return items
    
main()