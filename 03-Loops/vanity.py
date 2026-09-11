# str vanity
# start with letters 
# maximum 6 characters , minimum two characters
# end with two numbers
# first Number could not be zero
# no symbols allowed

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if not plate.isalnum():
        return False

    if not 2 <= len(plate) <= 6:
        return False

    if not plate[0].isalpha() or not plate[1].isalpha:
        return False

    for i in range(len(plate)):
        if plate[i].isdigit():
            if not plate[i] == '0':
                return False
            if not plate[i:].isdigit():
                return False
    
    return True

main()