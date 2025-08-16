import math

def naturals0(n):
    if n<0:
        raise ValueError("the number must be positive")
    first_n_naturals=[]
    for i in range(n+1):
        first_n_naturals.append(i)
    return first_n_naturals

def naturals(n):
    if n<0:
        raise ValueError("the number must be positive")
    first_n_naturals=[]
    for i in range(1,n+1):
        first_n_naturals.append(i)
    return first_n_naturals

def odd_numbers_up_to(n):
    if n<0:
        raise ValueError("the number must be positive")
    odds=[]
    for i in range(1,n+1,2):
        odds.append(i)
    return odds

def first_odd_numbers(n):
    if n<0:
        raise ValueError("the number must be positive")
    first_odds=[]
    for i in range(0,n):
        first_odds.append(i*2+1)
    return first_odds

def even_numbers_up_to(n):
    if n<0:
        raise ValueError("the number must be positive")
    odds=[]
    for i in range(0,n,2):
        odds.append(i)
    return odds

def first_even_numbers(n):
    if n<0:
        raise ValueError("the number must be positive")
    first_odds=[]
    for i in range(0,n):
        first_odds.append(i*2)
    return first_odds

def perfect_squares_up_to(n):
    if n<0:
        raise ValueError("the number must be positive")
    perfect_squares=[]
    last=int(math.sqrt(n))
    for i in range (last+1):
        perfect_squares.append(i*i)
    return perfect_squares

def first_perfect_square_numbers(n):
    if n<0:
        raise ValueError("the number must be positive")
    first_perfect_sqrt_numbers=[]
    for i in range(n):
        first_perfect_sqrt_numbers.append(i*i)
    return first_perfect_sqrt_numbers

def perfect_cubes_up_to(n):
    if n<0:
        raise ValueError("the number must be positive")
    perfect_cubes=[]
    last=int(math.cbrt(n))
    for i in range (last+1):
        perfect_cubes.append(i**3)
    return perfect_cubes

def first_perfect_cube_numbers(n):
    if n<0:
        raise ValueError("the number must be positive")
    first_perf_cube_numbers=[]
    for i in range(n):
        first_perf_cube_numbers.append(i**3)
    return first_perf_cube_numbers

def triangular_numbers_up_to(n):
    if n<0:
        raise ValueError("the number must be positive")
    triang_numbers=[]
    ok=1
    start=1
    while ok==1:
        triang_number=int(start*(start+1)/2)
        if triang_number>n:
            ok=0
        else:
            start=start+1
            triang_numbers.append(triang_number)
    return triang_numbers

def first_triangular_numbers(n):
    if n<0:
        raise ValueError("the number must be positive")
    first_triang_numbers=[]
    for i in range(1, n+1):
        first_triang_numbers.append(int(i*(i+1)/2))
    return first_triang_numbers

def tetrahedral_numbers_up_to(n):
    if n<0:
        raise ValueError("the number must be positive")
    tetr_numbers=[]
    ok=1
    start=1
    while ok==1:
        tetr_number=int(start*(start+1)*(start+2)/6)
        if tetr_number>n:
            ok=0
        else:
            start=start+1
            tetr_numbers.append(tetr_number)
    return tetr_numbers

def first_tetrahedral_numbers(n):
    if n<0:
        raise ValueError("the number must be positive")
    first_tetr_numbers=[]
    for i in range(1,n+1):
        first_tetr_numbers.append(int(i*(i+1)*(i+2)/6))
    return first_tetr_numbers

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    max_div = int(math.sqrt(n)) + 1
    for i in range(5, max_div, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def prime_numbers_up_to(n):
    if n<0:
        raise ValueError("the number must be positive")
    prime_numbers=[]
    for i in range(1,n+1):
        if isPrime(i):
            prime_numbers.append(i)
    return prime_numbers

def first_prime_numbers(n):
    if n<0:
        raise ValueError("the number must be positive")
    first_prime_nbrs=[]
    contor=1
    start=2
    while contor<=n:
        if isPrime(start):
            first_prime_nbrs.append(start)
            contor=contor+1
        start=start+1
    return first_prime_nbrs

def fibonacci_numbers_up_to(n):
    if n < 0:
        raise ValueError("the number must be positive")
    fib_numbers = [0, 1]
    while True:
        next_fib = fib_numbers[-1] + fib_numbers[-2]
        if next_fib > n:
            break
        fib_numbers.append(next_fib)
    return fib_numbers


def first_fibonacci_numbers(n):
    if n < 2:
        raise ValueError("the number must be greater than 1")
    first_fib_numbers = [0, 1]
    for _ in range(n - 2):
        next_fib = first_fib_numbers[-1] + first_fib_numbers[-2]
        first_fib_numbers.append(next_fib)
    return first_fib_numbers

def lucas_numbers_up_to(n):
    if n < 0:
        raise ValueError("the number must be positive")
    lucas_numbers = [2, 1]
    while True:
        next_fib = lucas_numbers[-1] + lucas_numbers[-2]
        if next_fib > n:
            break
        lucas_numbers.append(next_fib)
    return lucas_numbers


def first_lucas_numbers(n):
    if n < 2:
        raise ValueError("the number must be greater than 1")
    first_lucas_numbers = [2, 1]
    for _ in range(n - 2):
        next_fib = first_lucas_numbers[-1] + first_lucas_numbers[-2]
        first_lucas_numbers.append(next_fib)
    return first_lucas_numbers


def catalan_numbers_up_to(n):
    if n < 0:
        raise ValueError("the number must be positive")
    catalan_numbers=[]
    start=0
    while True:
        C=int((math.factorial(2*start)) / (math.factorial(start+1)*math.factorial(start)))
        if C<=n:
            catalan_numbers.append(C)
            start+=1
        else:
            break
    return catalan_numbers

def first_catalan_numbers(n):
    if n < 0:
        raise ValueError("the number must be positive")
    first_catalan_nbrs=[]
    for i in range(0,n):
        C=int((math.factorial(2*i)) / (math.factorial(i+1)*math.factorial(i)))
        first_catalan_nbrs.append(C)
    return first_catalan_nbrs

def factorial_numbers_up_to(n):
    if n < 0:
        raise ValueError("the number must be positive")
    start=1
    fact_numbers=[1]
    while True:
        nr=fact_numbers[start-1]*start
        if nr<=n:
            fact_numbers.append(nr)
            start+=1
        else:
            break
    return fact_numbers

def first_factorial_numbers(n):
    if n < 0:
        raise ValueError("the number must be positive")
    first_fact_numbers=[]
    if n==1:
        first_fact_numbers.append(1)
        return first_fact_numbers
    first_fact_numbers.append(1)
    for i in range(n-1):
        first_fact_numbers.append(first_fact_numbers[i]*(i+1))
    return first_fact_numbers

def padovan_numbers_up_to(n):
    if n < 0:
        raise ValueError("the number must be positive")
    if n==0 :
        raise ValueError("the number must be greater than 0")
    padovan_nbrs=[1,1,1]
    contor=3
    while True:
        new_number=padovan_nbrs[contor-2]+padovan_nbrs[contor-3]
        if new_number<=n:
            padovan_nbrs.append(new_number)
            contor+=1
        else:
            break
    return padovan_nbrs

def first_padovan_numbers(n):
    if n < 0:
        raise ValueError("the number must be positive")
    first_padovan_nbrs=[]
    if n==0:
        return first_padovan_nbrs
    first_padovan_nbrs.append(1)
    if n==1:
        return first_padovan_nbrs
    first_padovan_nbrs.append(1)
    if n==2:
        return first_padovan_nbrs
    first_padovan_nbrs.append(1)
    if n==3:
        return first_padovan_nbrs
    for i in range(3,n):
        first_padovan_nbrs.append(first_padovan_nbrs[i-2]+first_padovan_nbrs[i-3])
    return first_padovan_nbrs

def perrin_numbers_up_to(n):
    if n < 0:
        raise ValueError("the number must be positive")
    if n==0 :
        raise ValueError("the number must be greater than 0")
    perrin_nbrs=[3,0,2]
    contor=3
    while True:
        new_number=perrin_nbrs[contor-2]+perrin_nbrs[contor-3]
        if new_number<=n:
            perrin_nbrs.append(new_number)
            contor+=1
        else:
            break
    return perrin_nbrs

def first_perrin_numbers(n):
    if n < 0:
        raise ValueError("the number must be positive")
    first_perrin_nbrs=[]
    if n==0:
        return first_perrin_nbrs
    first_perrin_nbrs.append(3)
    if n==1:
        return first_perrin_nbrs
    first_perrin_nbrs.append(0)
    if n==2:
        return first_perrin_nbrs
    first_perrin_nbrs.append(2)
    if n==3:
        return first_perrin_nbrs
    for i in range(3,n):
        first_perrin_nbrs.append(first_perrin_nbrs[i-2]+first_perrin_nbrs[i-3])
    return first_perrin_nbrs