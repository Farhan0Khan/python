def main():
    time = input("What's time right now ? ")
    newTime = convert(time)
    print(newTime)
    
    if 7.0 <= newTime <= 8.0:
        print('it is breakfast time')
    elif 12.0 <= newTime <= 13.0:
        print('it is lunch time')
    elif 19.0 <= newTime <= 20.0:
        print('it is dinner time')

def convert(t):
    h , m = t.split(':')
    return float(h) + (float(m) / 60)

main()