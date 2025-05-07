class Solution:
    def evaluate(self, expr):
        chars = expr.split()
        reversedChars = reversed(chars)

        stack = []

        for c in reversedChars:
            print(c)
            
            if c not in '+-*/':
                stack.append(c)
                print(stack)
                continue
                    
            b = int(stack.pop())
            a = int(stack.pop())

            if c == '+':
                stack.append(b+a)
            elif c == '-':
                stack.append(b-a)
            elif c == '*':
                stack.append(b*a)
            elif c == '/':
                stack.append(b//a)


            print(stack)

        return stack[0]
            
            


