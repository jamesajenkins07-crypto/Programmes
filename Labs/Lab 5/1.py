def factorial(n):
    answer = 1
    for factor in range(1, (n+1)):
        answer *= factor
    return answer

print(factorial(3))
print(factorial(5))
