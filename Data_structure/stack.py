# stack은 list로 구현
# last in first out

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
print(stack[0:])
print(stack[:])


print(stack[::-1])


print(pop_value1)
print(pop_value2)