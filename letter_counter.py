'''
counter = letter_counter('Amazing')
counter('a') # 2
counter('m') # 1

counter2 = letter_counter('This Is Really Fun!')
counter2('i') # 2
counter2('t') # 1 
'''

def letter_counter(sentence):
    sentence_inner=sentence.lower()
    
    
    def inner(letter):
        count = {val: sentence_inner.count(val) for val in sentence_inner}
        return count[letter]
    
    return inner
