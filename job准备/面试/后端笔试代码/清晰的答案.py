class Solution:
    def calculate(self, s: str) -> int:
        stack_num = []
        stack_opt = []
        i = 0
        priorty = {'(':0,')':0,'+':1,'-':1,'*':2,'/':2}
        while i<len(s):
            if s[i]==' ':
                i += 1
                continue
            if '0'<=s[i]<='9':
                j = i
                while i+1<len(s) and '0'<=s[i+1]<='9':
                    i += 1
                num = int(s[j:i+1])
                stack_num.append(num)
            elif s[i]=='(':
                stack_opt.append(s[i])
            elif s[i]==')':
                while stack_opt[-1]!='(':
                    opt = stack_opt.pop()
                    A = stack_num.pop()
                    B = stack_num.pop()
                    res = self.calc(A,B,opt)
                    stack_num.append(res)
                stack_opt.pop()
            else:
                while stack_opt and priorty[stack_opt[-1]]>=priorty[s[i]]:
                    opt = stack_opt.pop()
                    A = stack_num.pop()
                    B = stack_num.pop()
                    res = self.calc(A,B,opt)
                    stack_num.append(res)
                stack_opt.append(s[i])
            i += 1

        while stack_opt:
            opt = stack_opt.pop()
            A = stack_num.pop()
            B = stack_num.pop()
            res = self.calc(A,B,opt)
            stack_num.append(res)
        return stack_num[-1]
    
    def calc(self,num1,num2,opt):
        if opt=='+':
            return int(num1)+int(num2)
        elif opt=='-':
            return int(num2)-int(num1)
        elif opt=='*':
            return int(num2)*int(num1)
        elif opt=='/':
            return int(num2)//int(num1)


s = Solution()
expression = '2+8/2*(5+5+3)*2'
result = s.calculate(expression)
print(result)





""" 解题思路
双栈法，stack_num记录数字，stack_opt记录操作符。首先来看一种最基本的计算操作：stack_num中pop出来两个数A,B, stack_opt中pop出来一个操作符opt, 计算结果为B opt A, 将结果存到stack_num中。

字符有以下几种情况：

空格，直接下一个字符。
数字，直接入stack_num栈。需要注意处理多位数。
'(', 直接入stack_opt栈
')', 重复最基本的计算操作，直到stack_opt栈栈顶为')'。然后stack_opt栈pop出来')'。
操作符，如果栈顶操作符的优先级大于等于当前操作符的优先级，则重复最基本的计算操作，直到stack_opt栈空或者其栈顶操作符的优先级小于当前操作符的优先级，再将当前操作符入stack_num栈。优先级定义priorty = {'(':0,')':0,'+':1,'-':1,'*':2,'/':2}。数字越大，优先级与越高。
在遍历完所有字符后，判断当前操作栈stack_opt是否为空,不为空，重复最基本的计算操作，知道操作栈为stack_opt为空。最后结果就是stack_num中剩余的唯一一个元素。
 """