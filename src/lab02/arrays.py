import ast
m = input()
def min_max(m: list[float | int]) -> tuple[float | int, float | int]:
    m = ast.literal_eval(m)
    if m==[]:
        raise ValueError('пустой список')
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

def unique_sorted(m: list[float | int]) -> list[float | int]:
    m = ast.literal_eval(m)
    ans = list(set(m))
    for i in range(len(ans)-1):
        for i in range(len(ans)-1):
            fl = True
            if ans[i]> ans[i+1]:
                ans[i],ans[i+1] = ans[i+1],ans[i]
                fl = False
        if fl:
            break
    return ans

def flatten(m: list[list | tuple]) -> list:
    m = ast.literal_eval(m)
    ans = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if isinstance(m[i][j], (int, float)):
                ans.append(m[i][j])
            else:
                raise TypeError('строка не строка строк матрицы')
    return ans
    
#print(min_max(m))
#print(unique_sorted(m))
print(flatten(m))