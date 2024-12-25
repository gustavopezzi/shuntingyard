#################################################################
# Input expression (tokens separated by spaces)
#################################################################
input = "( 3 + 4 ) * 2 / ( ( 1 - ( 5 ) ) ^ 2 ) ^ 3 + 4"

#################################################################
# Define operator precedence level and their associativity
#################################################################
precedence = {
  '^': 4,
  '*': 3,
  '/': 3,
  '+': 2,
  '-': 2
}

rightassoc = {
  '^': True,
  '*': False,
  '/': False,
  '+': False,
  '-': False
}

#################################################################
# Perform Shunting-Yard algorithm
#################################################################
output = []
opstack = []

for token in input.strip().split():
  if token == '(':
    opstack.append(token)
  elif token == ')':
    while len(opstack) > 0:
      op = opstack.pop()
      if op == '(':
        break
      output.append(op)
  else:
    if token in precedence:
      while len(opstack) > 0:
        op = opstack[-1]
        if op == '(':
          break
        if precedence[token] > precedence[op] or (rightassoc[token] == True and (precedence[token] == precedence[op])):
          break
        opstack.pop()
        output.append(op)
      opstack.append(token)
    else:
      output.append(token)

# Push the remaining operators from the opstack into the output
while len(opstack) > 0:
  output.append(opstack.pop())

print("POSTFIX (RPN):", ','.join(output))

#################################################################
# Evaluate a list of elements (in postfix notation / RPN form)
#################################################################
result = []
for elem in output:
  if elem not in precedence:
    result.append(float(elem))
  else:
    right = result.pop()
    left = result.pop()
    if elem == '+':
      result.append(left + right)
    if elem == '-':
      result.append(left - right)
    if elem == '*':
      result.append(left * right)
    if elem == '/':
      result.append(left / right)
    if elem == '^':
      result.append(left ** right)

print("RESULT:", result.pop())
