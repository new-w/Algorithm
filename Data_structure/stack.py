# stack은 list로 구현

stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
pop_value1 = stack.pop()
stack.append(1)
stack.append(4)
pop_value2 = stack.pop()

print(stack)
print(pop_value1)
print(pop_value2)