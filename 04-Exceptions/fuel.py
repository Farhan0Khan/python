def main():
    f = get_fraction('➗Fraction: ')
    r = check_fuel(f)
    
    if r <= 1:
        print(f"⛽Fuel: E 🚨")
    elif r >= 99:
        print(f"⛽Fuel: F 👍")
    else:
        print(f"Fuel: {r}%")

def get_fraction(prompt):
    while True:
        try:
            i = input(prompt)
            x , y = i.split("/")
            x = int(x)
            y = int(y)
            if x < 0 or y <= 0 or x > y:
                raise ValueError()
            else:
                return (x , y)
        except ValueError:
            print('Invalid Fraction ⚠️')
        
        

def check_fuel(f):
    return round((f[0] / f[1] ) * 100)

main()