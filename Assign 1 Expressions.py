from Stacks import Stack
from Stacks import Node

def infixToPostfix(infixexpr):
    """Converts an infix expression to an equivalent postfix expression
       Signature:  a string containing an infix expression where tokens are space separated is
       the single input parameter and returns a string containing a postfix expression
       where tokens are space separated"""
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postfixList = []

    tokenList = infixexpr.split()

    for token in tokenList:
        print(token)
        if token not in "+-*/^()":    # assumes that input has been validated as operators or valid numerics
            postfixList.append(token)
        elif token in "(^":  # handles right associativity of ^
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:       #FIX THIS
            while (not opStack.is_empty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.is_empty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)


def postfixEval(postfixExpr):
    operandStack = Stack()

    tokenList = postfixExpr.split()

    for token in tokenList:
        if token not in "+-*/^()":
            operandStack.push(float(token))   # put a try and exception here
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)

    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    else:
        return op1 ** op2

def postfix_valid(infixexpr):

    tokenList = infixexpr.split()
    n_operands = 0
    n_operators = 0
    expr_valid = True
    if tokenList[0] in "+-*/^()" or tokenList[1] in "+-*/^()" :
        expr_valid = False
    else:
        n_operands =2

    for token in tokenList[2:len(tokenList)]:
        # print(token)
        if token  in "()":    # assumes that input has been validated as operators or valid numerics
            pass
        elif token in "+-*/^":
            n_operators += 1
        else:       
            n_operands += 1
        
        if n_operands - n_operators < 1:
           expr_valid = False
           break 

    return expr_valid

junk = "2 +"
print(junk)
print(postfix_valid(junk))

# infix_expr = "( 2.5 + 2.5 ) * 4 / 5 ^ 2"
infix_expr = " ( 2 ^ 3 ) ^ 2 "

postfix_expr = infixToPostfix(infix_expr)

print(postfixEval(postfix_expr))
