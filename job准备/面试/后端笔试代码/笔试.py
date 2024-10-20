def expression(strs: str):
    operation_num = []
    operation = []
    compare = ('+','-','*','/','(',')')
    for i in len(strs):
        if i in compare:
            operation.append(i)
        else:
            operation_num.append(i)
        
        

a = 'fdd'
b = '3'
print(a.isdigit())
print(b.isdigit())
print(int(3.55))

print((0-3)/4)

