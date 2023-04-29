'''
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
'''

# define mode below:
def mode(num):
    num.sort()
    maxcnt=0
    cnt=0
    numbero=0
    for i in range(0,len(num)-2):
        if num[i]==num[i+1]:
            cnt+=1
        elif num[i] != num[i+1]:
            if cnt > maxcnt:
                maxcnt=cnt
                numbero = num[i]
    return numbero
