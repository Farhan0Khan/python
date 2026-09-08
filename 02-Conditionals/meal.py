def main():
    # Ask user for time
    time = input('Enter Your time: ')

    # convert str to float
    t = convert(time)

    # check for meal time 
    if t >= 7.0 and t <= 8.0:
        print('breakfast time')
    elif t >= 12.0 and t <= 13.00:
        print('lunch time')
    elif t >= 18 and t <= 19.00:
        print('dinner time')
    else:
        print('there is some time left for next meal')



def convert(t):
    hours , minutes = t.split(':')
    return float(hours) + (float(minutes) / 60)

if __name__ == '__main__':
    main()
    