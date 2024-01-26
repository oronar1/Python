"""
This is simple textual translator To/From Morse code
"""

MORSE_CODE_DICT = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'--.',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    '0':'-----',
    '.':'.-.-.-',
    ',':'--..--',
    '?':'..--..',
    "'":'.----.',
    '!':'-.-.--',
    '/':'-..-.',
    '(':'-.--.',
    ')':'-.--.-',
    '&':'.-...',
    ':':'---...',
    ';':'-.-.-.',
    '=':'-...-',
    '+':'.-.-.',
    '-':'-....-',
    '_':'..--.-',
    '"':'.-..-.',
    '$':"...-..-",
    '@':'.--.-.',
    ' ': '/'
}

def text_to_morse(text):
    morse_code= ""
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += ' '
    return morse_code.strip()

def morse_to_text(morse_code):
    morse_to_char = {morse: char for char, morse in MORSE_CODE_DICT.items()}
    words = morse_code.split('   ')
    translated_text = ''
    for word in words:
        chars = word.split()
        for i,char in enumerate(chars):
            if i == 0:
                translated_text += morse_to_char.get(char, '').upper()
            else:
                translated_text += morse_to_char.get(char, '').lower()
        translated_text += ' '
    return translated_text.strip()

def main():
    finish = False
    while not finish:
        choice = input("Choose an option:\n1. Text to Morse Code\n2. Morse Code to Text\n3. Exit\nEnter choice (1/2/3):")
        match choice:
            case '1':
                input_text = input("Enter a string: ")
                morse_code = text_to_morse(input_text)
                print(f'Morse Code: {morse_code}')
            case '2':
                input_morse = input("Enter Morse Code: ")
                translated_text = morse_to_text(input_morse)
                print(f'Translated Text: {translated_text}')
            case '3':
                finish = True
            case '_':
                print("Invalid choice. Please Enter 1 or 2")

if __name__ == "__main__":
    main()
