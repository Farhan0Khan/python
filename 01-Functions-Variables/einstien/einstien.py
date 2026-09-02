def main():
    weight = float(input('Tell me Mass in kg! '))
    energy = energyConverter(weight)
    print(f"{energy:,}")

def energyConverter(mass):
    return mass * 300000000

main()