
import re

def is_valid_time(tim2check):
    pattern = re.compile('^\d\d?:\d\d$')
    match = pattern.search(tim2check)
    if match:
        return True
    return False
    
    
  # Function called is_valid_time  that accepts a single string argument. 
  # It should return True  if the string is formatted correctly as a time, like 3:15 or 12:48 and return False otherwise. 
  # Note that times can start with a single number (2:30) or two (11:18).  

   # is_valid_time("10:45")       #True
   # is_valid_time("1:23")        #True
   # is_valid_time("10.45")       #False
   # is_valid_time("1999")        #False
   # is_valid_time("145:23")      #False

# In order to return True, the string should ONLY contain the time, and no other characters

 #   is_valid_time("it is 12:15") #False
 #   is_valid_time("12:15")       #True
