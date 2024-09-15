import sys

braille_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO'
}
english_letters = {value: key for key, value in braille_letters.items()}

space = '......'
capital = '.....O'
number = '.O.OOO'
braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}
english_numbers = {value: key for key, value in braille_numbers.items()}

def translate(text):
    if isBraille(text): 
        return toEnglish(text)
    return toBraille(text)

def isBraille(text):
    for i in text:
        if i != 'O' and i != '.':
            return False
    return True

def toEnglish(word):
    letters = [word[i:i+6] for i in range(0, len(word), 6)]
    english_word = ''
    next_capital = False
    next_number = False
    for i in letters:
        if next_capital:
            english_word += english_letters[i].capitalize()
            next_capital = False
        elif i == space:
            if next_number:
                next_number = False
            english_word += ' '
        elif next_number:
            english_word += english_numbers[i]
        elif i == capital:
            next_capital = True
        elif i == number:
            next_number = True
        else: 
            english_word += english_letters[i]
    return english_word

def toBraille(word):
    braille_word = ''
    next_number = False
    for char in word:
        if char.isupper():
            braille_word += capital
            braille_word += braille_letters[char.lower()]
        elif char.isdigit(): 
            if not next_number:
                braille_word += number
                next_number = True
            braille_word += braille_numbers[char]
        elif char == ' ':
            next_number = False
            braille_word += space
        else: 
            braille_word+= braille_letters[char]
    return braille_word

if __name__ == "__main__":
    input_text = ' '.join(sys.argv[1:])
    print(translate(input_text))
