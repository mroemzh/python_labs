lst=input()
lst = lst.replace('[','')
lst = lst.replace(']','')
lst = lst.replace(',','')
def min_max(m):
    if m=='':
        raise ValueError('пустой список')
        return 
    m = list(map(float,m.split()))
    
    mn,mx = m[0],m[0]
    if len(m)==1:
        if m[0] == int(m[0]):
            return (int(m[0]),int(m[0]))
        return (m[0],m[0])
    for i in m:
        if i<mn:
            mn=i
        if i>mx:
            mx=i
    if int(mx) == mx:
        mx = int(mx)
    if int(mn) == mn:
        mn = int(mn)
    return (mn,mx)
def unique_sorted():
    m = list(map(float,m.split()))
    m = sorted
print(min_max(lst))
