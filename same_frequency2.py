  '''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''     
  def same_frequency(num1,num2):
    d1 = {letter:str(num1).count(letter) for letter in str(num1)}
    d2 = {letter:str(num2).count(letter) for letter in str(num2)}
    for key,val in d1.items():
      if not key in d2.keys():
        return False
      elif d2[key] != d1[key]:
        return False
      return True
