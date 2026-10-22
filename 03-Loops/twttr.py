def main():
    tweet_input = input("Input: ")
    print(f"Output: {convert_to_twttr(tweet_input)}")

def convert_to_twttr(twt):
    tweet_output = ''

    for i in twt:
        if i not in ['a' , 'i' , 'o' , 'e',  'u'] and i not in ['A', 'I' , 'O' , 'E' , 'U']:
            tweet_output += i
    
    return tweet_output


main()