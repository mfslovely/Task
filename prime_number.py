def is_prime(n):
    if n <=1:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True
    
n = 13
<<<<<<< HEAD
print(is_prime(n))
=======
print(is_prime(n))


# find dbulicate

l = [1,2,3,44,55,55,66,7]
result = []

for i in l:
    if i not in result:
        result.append(i)

print(result)
>>>>>>> my_branch

# even number

n = 4

if n % 2 == 0:
    print("yes")
