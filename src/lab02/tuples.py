import ast
m = ast.literal_eval(input())

def format_record(rec: tuple[str, str, float]) -> str:
    ans = ''
    p1 = list(map(str,m[0].split()))
    if len(p1) < 2:
        raise ValueError('некорректное фио')
    p2 = str(m[1])
    if p2 == '':
        raise ValueError('пустая группа')
    try:
        p3 = float(m[2])
    except: ValueError('некорректный балл')
    ans = p1[0][0].upper() + p1[0][1:] +' '+ p1[1][0].upper()+'.'
    if len(p1) == 3:
        ans = ans + p1[2][0].upper()+'.,'
    else:
        ans = ans + ','

    ans = ans + ' гр. ' + p2 + ', GPA ' + str("{:.2f}".format(p3))
    print(ans)
format_record(m)