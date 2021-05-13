# Finding precedence of operators.
def precedence(operation):
    if operation == '+' or operation == '-':
        return 1
    if operation == '*' or operation == '/':
        return 2
    if operation == '^':
        return 3
    return 0

#Perform arithmetic operations
def applyOp(x, y, operation):
    if operation == '+': return x + y
    if operation == '-': return x - y
    if operation == '*': return x * y
    if operation == '/': return x / y
    if operation == '^': return pow(x,y)

# Function that returns value of expression after evaluation.
def evaluate(tokens):

	# stack to store integer values.
	values = []
	
	# stack to store operators.
	ops = []
	i = 0
	
	try:
		while i < len(tokens):
			# if current token is a whitespace, # skip it.
			if tokens[i] == ' ':
				i += 1
				continue
			
			# Current token is an opening # brace, push it to 'ops'
			elif tokens[i] == '(':
				ops.append(tokens[i])
			
			# Current token is a number, push it to stack for numbers.
			elif tokens[i].isdigit():
				val = 0

				# There may be more than one, digits in the number.
				while (i < len(tokens) and (tokens[i].isdigit() or tokens[i] == ".")):
					#detecting the point
					if tokens[i] == ".":
						i += 1
						k = i
						y = 1
						#looping through the floating point numbers and adding them.
						while (k < len(tokens) and tokens[k].isdigit()):
							y = y * 10
							val = val + (float(tokens[k]) * (1/y))
							k += 1
						i = k
					else:  
						val = (val * 10) + int(tokens[i])
						i += 1
				values.append(val)
				
				# right now the i points to the character next to the digit, 
				# since the for loop also increases the i, we would skip one
				# token position; we need to
				# decrease the value of i by 1 to
				# correct the offset.
				i-=1
			
			# Closing brace encountered,
			# solve entire brace.
			elif tokens[i] == ')':
			
				while len(ops) != 0 and ops[-1] != '(':
				
					val2 = values.pop()
					val1 = values.pop()
					op = ops.pop()
					
					values.append(applyOp(val1, val2, op))
				
				# pop opening brace.
				ops.pop()
			
			# Current token is an operator.
			else:
			
				# While top of 'ops' has same or
				# greater precedence to current
				# token, which is an operator.
				# Apply operator on top of 'ops'
				# to top two elements in values stack.
				while (len(ops) != 0 and precedence(ops[-1]) >= precedence(tokens[i])):		
					val2 = values.pop()
					val1 = values.pop()
					op = ops.pop()
					
					values.append(applyOp(val1, val2, op))
				
				# Push current token to 'ops'.
				ops.append(tokens[i])
			
			i += 1
		
		# Expression has been calc at this point, apply remaining ops to remaining values.
		while len(ops) != 0:
			
			val2 = values.pop()
			val1 = values.pop()
			op = ops.pop()
					
			values.append(applyOp(val1, val2, op))
		
		#Top of values contains result, return it.
		return values[-1]
	except IndexError as e:
		return "wrong input"

# Driver Code
if __name__ == "__main__":

	while True:
		val = input("Enter your expression: ")
		
		if(val == 'exit'):
			print('Calculator terminated')
			break
		else:
			result = evaluate(val)
			if (result == "wrong input"):
				print("Syntax Error, Check expression\n")
			else:
				precision = input("Enter the level of precision: ")
				pre = "%." + precision + "f"
				print(pre % result)
				print("\n")
			
