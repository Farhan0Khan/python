name = input("What's Your name ? ")

match name:
    case 'Harry' | 'Hermoinee' | 'Ron':
        print('Gryffindoor')
    case 'Draco':
        print('Slytherine')
    case _:
        print('Who')