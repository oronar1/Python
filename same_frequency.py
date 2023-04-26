
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
