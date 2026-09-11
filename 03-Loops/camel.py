# program to convert camelCase to snake_case

def main():
    variable = input('camelCase: ')
    camel_case_to_snake_case(variable)


def camel_case_to_snake_case(variable):
    j = ''
    for i in variable:
        if i.isupper():
            j += '_'
            i = i.lower()
        j += i
    print(f'snake_case: {j}')
    
        

main()

