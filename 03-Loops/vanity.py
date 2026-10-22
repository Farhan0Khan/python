# start with at least two letters
# may contain max of 6 characters and min 2 
# numbers must be come at the end
# first number cannot be 0 
# only numbers and characters are allowed


def main():
    vanity = input("Plate: ")
    result = validate_vanity(vanity)  
    print(result)

def validate_vanity(v):
    v = list(v)
    if (
        2 <= len(v) <= 6 or 
        v[0].isalpha() or 
        v[1].isalpha() or 
        v[len(v)].isdigit()
    ):
        return 'Valid'
    else:
        return 'Invalid'

main()