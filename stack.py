stack = [1,2,4,5,6,7,8,9,10]
print(stack)
# 10 ujung stack

n2 = 11

stack.append(n2)
print(stack)

taken = stack.pop(stack[2])
print(taken)
print(stack)

jumlah = len(stack)
print(jumlah)

if jumlah == 0:
    isEmpty = True
else:
    isEmpty = False

print(isEmpty)
