def main():
    dollar = dollarToFloat(str(input("Enter Amount? ")))
    percentage = percentToFloat(str(input('Enter tip percent? ')))
    tip = tipCalculate(dollar , percentage)
    print("Your tip is", tip)

def tipCalculate(amount , percent):
    result = amount + (amount * (percent / 100))
    return result
    

def dollarToFloat(v):
    v = v.replace('$', '')
    v = float(v)
    return v

def percentToFloat(v):
    v = v.replace('%', '')
    v = float(v)
    return v

main()