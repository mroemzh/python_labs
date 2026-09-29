import ast
m = ast.literal_eval(input())
width = 0
if m!=[]:
    width = len(m[0])
else:
    width=0
height = len(m)

def transpose(m: list[list[float | int]]) -> list[list]:
    ans = []
    for i in range(width):
        t = []
        for j in range(height):
            t.append(m[j][i])
        ans.append(t)
    return ans

def row_sums(m: list[list[float | int]]) -> list[float]:
    ans = []
    for i in range(height):
        ans.append(sum(m[i]))
    return ans

def col_sums(m: list[list[float | int]]) -> list[float]:
    global width, height
    mm = transpose(m)
    height,width = width,height
    return row_sums(mm)

for i in range(height):
    if len(m[i])!= width:
        raise ValueError('рваная матрица')

#print(transpose(m))
#print(row_sums(m))
print(col_sums(m))
