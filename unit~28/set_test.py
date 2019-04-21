input1, input2 = map(int, input().split())

a = {i for i in range(1, input1+1) if input1%i == 0}
b = {i for i in range(1, input2+1) if input2%i == 0}

divisor = a & b
 
result = 0
if type(divisor) == set:
    result = sum(divisor)
 
print(result)