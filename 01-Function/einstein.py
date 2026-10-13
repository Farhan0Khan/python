def main():
    mass = int(input('Enter amount of mass in kg: '))
    calculateEnergy(mass)

def calculateEnergy(m):
    c = 3 * 100000000
    e = c * m 
    print(f"calculated energy is {e} joules")

main()