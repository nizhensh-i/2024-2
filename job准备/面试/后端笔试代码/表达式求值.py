
def calculate(expression):
    num_stack = []
    op_stack = []

    # 判断运算符的优先级
    def priority(op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0

    def operate():
        b = num_stack.pop()
        a = num_stack.pop()
        op = op_stack.pop()
        if op == '+':
            num_stack.append(a + b)
        elif op == '-':
            num_stack.append(a - b)
        elif op == '*':
            num_stack.append(a * b)
        elif op == '/':
            num_stack.append(a / b)

    i = 0
    while i < len(expression):
        if expression[i].isdigit():  # 数字
            num = 0
            # 该数字位数>1 处理多位数
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            num_stack.append(num)
        elif expression[i] == '(' or (expression[i] in '+-*/' and (not op_stack or op_stack[-1] == '(')):
            op_stack.append(expression[i])
            i += 1
        elif expression[i] == ')':
            while op_stack[-1] != '(':
                operate()
            op_stack.pop()  # 弹出‘(’
            i += 1
        else:
            while op_stack and priority(op_stack[-1]) >= priority(expression[i]):
                operate()
            op_stack.append(expression[i])
            i += 1

    while op_stack:
        operate()

    return num_stack[-1]

expression = '2+8/2*(5+5+3)'
result = calculate(expression)
print(f"计算结果为：{result}")
