def main():
    fileName = input('Enter the filename: ')
    checkFileType(fileName)

def checkFileType(f):
    a, b = f.split('.')
    
    if b == 'gif' or b == 'png' or b == 'jpeg' or b == 'jpg':
        print(f"image/{b}")
    elif b == '.mp4':
        print(f"video/{b}")
    elif b == 'txt':
        print(f"textfile/{b}")
    elif b == 'pdf':
        print(f"pdf file")
    
main()