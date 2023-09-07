import pandas as pd

message = input('<Enter message> ')
message = message.upper().replace('J', 'I')

dblkey = input('<Enter double key> ')
dblkey = dblkey.upper().replace('J', 'I')

data = [['A','B','C','D','E'],
        ['F','G','H','I','K'],
        ['L','M','N','O','P'],
        ['Q','R','S','T','U'],
        ['V','W','X','Y','Z']]

df = pd.DataFrame(data, columns=[1,2,3,4,5])
df = df.set_axis(range(1, len(df)+1))

code = []
for i in range(0,len(message)):
    for x in range(1,6):
        for y in range(0,5):
            if df[x].iloc[y]==message[i]:
                code.append(str(df.index[y])+str(x))
code = [int(a) for a in code]

code2 = []
for i in range(0,len(dblkey)):
    for x in range(1,6):
        for y in range(0,5):
            if df[x].iloc[y]==dblkey[i]:
                code2.append(str(df.index[y])+str(x))
code2 = [int(a) for a in code2]

code3 = []
for c in range(0,len(code)):
    code3.append(code2[c%len(code2)]+code[c])

print(str(code3).replace(', ','-').replace('[','').replace(']',''))
