def main():
    l1 = [1 , 2 , 3 , 4 ,-1 , 5 , 6 , 0 , 9]
    print(f"Min = {min(l1)}\nMax = {max(l1)}\nSum = {sum(l1)}\nAverage = {sum(l1) / len(l1)}")


    # to print even and Odd
    Odd = 0
    Even = 0
    for i in l1:
        if i % 2 == 0:
            Even += 1
        else:
            Odd += 1
    print(f"Odd = {Odd}\nEven = {Even}")

    # to search elements
    print(search(l1 , 3))

    # to check duplicates
    print(has_duplicates(l1))

    # sorting in ascending order 
    print(sorted(l1))

    # sort in descending order
    newl1 = sorted(l1)
    newl1.reverse()
    print(newl1)

    # to find second largest
    if has_duplicates(newl1):
        if newl1[0] == newl1[1]:
            print(f"second largest = {newl1[2]}")
    else:
        print(f"second largest = {newl1[1]}")

# to search from the list
def search(tup , target):
    for i , num in enumerate(tup):
        if num == target:
            return i
    return -1


# to check if list has duplicates
def has_duplicates(tup):
    seen = []
    for num in tup:
        if num in seen:
            return True
        seen.append(num)
    return False

# to remove duplicates
def remove_duplicates(tup):
    unique = []
    for num in tup:
        if num not in unique:
            unique.append(num)
        return unique

main()

        
