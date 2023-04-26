'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''
def same_frequency(num1,num2):
    lst1=list(map(int, str(num1)))
    lst2=list(map(int, str(num2)))
    lst1.sort()
    lst2.sort()
    if len(lst1)==len(lst2):
        for x,val in enumerate(lst1):
            if lst1[x]!=lst2[x]:
                return False
        return True
    return False
