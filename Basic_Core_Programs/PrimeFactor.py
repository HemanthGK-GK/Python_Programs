# Computes the prime factorization of N using brute force
def primeFactors(num):
    i = 2
    factors = []
    #loop for checking factors of num
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors
    
#calling function
print(primeFactors(15))