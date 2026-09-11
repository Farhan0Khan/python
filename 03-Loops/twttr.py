text = input('Input: ')

new_word = ''

for char in text:
    if char not in 'AEIOUaeiou':
        new_word += char

print('Output:', new_word)