'''
reverse_vowels("Hello!") # "Holle!" 
reverse_vowels("Tomatoes") # "Temotaos" 
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
'''

def reverse_vowels(sentence):
    vowels='aeiou'
    string=list(sentence)
    i , j = 0 , len(sentence)-1
    while i<j:
        if string[i].lower() not in vowels:
            i+=1
        elif string[j].lower() not in vowels:
            j-=1
        else:
            string[i],string[j] = string[j], string[i]
            i+=1
            j-=1
    return "".join(string)
