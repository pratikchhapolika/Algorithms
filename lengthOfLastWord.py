def lengthOfLastWord(A):
    if len(A)==0:
        return 0
    if A.isspace():
        return 0
    l=[]
    l=A.split(' ')
    l=[i for i in l if i.strip()]
    n=len(l)-1
    return len(l[n])

lengthOfLastWord("yash    ")