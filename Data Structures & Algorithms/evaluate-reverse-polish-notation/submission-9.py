class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[-1])

        stack = []
        for token in tokens:
            if stack and token in '-+/*':
                post_op, pre_op = int(stack.pop()), int(stack.pop())
                if token == '+':
                    stack.append(post_op + pre_op)
                elif token == '-':
                    stack.append(pre_op - post_op)
                elif token == '/':
                    stack.append(int(pre_op / post_op))
                else:
                    stack.append(pre_op * post_op)
            else:
                stack.append(token)
        
        return stack[-1]