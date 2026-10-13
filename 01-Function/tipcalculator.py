def main():
    dollar = dollarsToFloat(input('How much was the meal? '))
    percent = percentageToFloat(input('what percentage would you like to tip? '))
    tip = dollar * percent
    print(f"Bill ${dollar: .2f}")
    print(f"Tip ${tip: .2f}")
    print(f"Total ${(tip + dollar): .2f}")

def dollarsToFloat(i):
    i = i.removeprefix('$')
    i = float(i)
    return i

def percentageToFloat(i):
    i = i.removesuffix('%')
    i = float(i)
    i = i / 100
    return i 

main()