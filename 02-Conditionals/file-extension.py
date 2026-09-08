def main():
    filename = str(input('File Name: '))
    if checkFileType(filename):
        print('it is an Image file')
    else:
        print('it is a document')


def checkFileType(f):
    if f.endswith('.png') or f.endswith('.jpeg') or f.endswith('.jpg') or f.endswith('.gif'):
        return True
    elif f.endswith('.pdf') or f.endswith('.txt') or f.endswith('.zip'):
        return False

main()