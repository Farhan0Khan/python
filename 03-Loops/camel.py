def main():
    camelCase = input("camelCase: ")
    convert_to_snake_case(camelCase)


def convert_to_snake_case(c):
    snk = list(c)
    for i in range(len(snk)):
        if snk[i] == snk[i].upper():
            snk[i] = snk[i].lower()
            snk.insert(i , "_")
    print(f"snake_case = {"".join(snk)}")
    

main()