numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i > 1:
        for k in 2, 3:
                if i % k == 0 and i / k > 1 :
                    not_primes.append(i)
                    break
        else:
            primes.append(i)

print('not_primes:', not_primes)
print('primes:', primes)












