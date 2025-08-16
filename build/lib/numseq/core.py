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

def motzkin_numbers_up_to(n):
    if n < 0:
        raise ValueError("the number must be positive")
    if n == 0:
        raise ValueError("the number must be greater than 0")

    motzkin_nbrs = [1, 1]
    i = 2
    while True:
        next_val = motzkin_nbrs[i-1] + sum(motzkin_nbrs[k] * motzkin_nbrs[i-2-k] for k in range(i-1))
        if next_val <= n:
            motzkin_nbrs.append(next_val)
            i += 1
        else:
            break
    return motzkin_nbrs


def first_motzkin_numbers(n):
    if n < 0:
        raise ValueError("the number must be positive")
    if n == 0:
        return []
    if n == 1:
        return [1]
    motzkin_nbrs = [1, 1]
    for i in range(2, n):
        motzkin_nbrs.append(motzkin_nbrs[i-1] + sum(motzkin_nbrs[k] * motzkin_nbrs[i-2-k] for k in range(i-1)))
    return motzkin_nbrs

def tribonacci_numbers_up_to(n):
    if n < 0:
        raise ValueError("the number must be positive")
    if n == 0:
        raise ValueError("the number must be greater than 0")

    trib_nbrs = [0, 1, 1]  # T(0)=0, T(1)=1, T(2)=1
    i = 3
    while True:
        new_number = trib_nbrs[i-1] + trib_nbrs[i-2] + trib_nbrs[i-3]
        if new_number <= n:
            trib_nbrs.append(new_number)
            i += 1
        else:
            break
    return trib_nbrs


def first_tribonacci_numbers(n):
    if n < 0:
        raise ValueError("the number must be positive")
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    trib_nbrs = [0, 1, 1]
    for i in range(3, n):
        trib_nbrs.append(trib_nbrs[i-1] + trib_nbrs[i-2] + trib_nbrs[i-3])
    return trib_nbrs

def armstrong_numbers_up_to(n):
    if n < 0:
        raise ValueError("the number must be positive")
    if n == 0:
        raise ValueError("the number must be greater than 0")

    armstrong_nbrs = []
    for num in range(1, n+1):
        power = len(str(num))
        if num == sum(int(digit) ** power for digit in str(num)):
            armstrong_nbrs.append(num)
    return armstrong_nbrs


def first_armstrong_numbers(n):
    if n < 0:
        raise ValueError("the number must be positive")
    armstrong_nbrs = []
    num = 1
    while len(armstrong_nbrs) < n:
        power = len(str(num))
        if num == sum(int(digit) ** power for digit in str(num)):
            armstrong_nbrs.append(num)
        num += 1
    return armstrong_nbrs

def perfect_numbers_up_to(n):
    if n < 0:
        raise ValueError("the number must be positive")
    if n == 0:
        raise ValueError("the number must be greater than 0")

    perfect_nbrs = []
    for num in range(2, n+1):
        divisors_sum = sum(d for d in range(1, num//2 + 1) if num % d == 0)
        if divisors_sum == num:
            perfect_nbrs.append(num)
    return perfect_nbrs


def first_perfect_numbers(n):
    if n < 0:
        raise ValueError("the number must be positive")
    perfect_nbrs = []
    num = 2
    while len(perfect_nbrs) < n:
        divisors_sum = sum(d for d in range(1, num//2 + 1) if num % d == 0)
        if divisors_sum == num:
            perfect_nbrs.append(num)
        num += 1
    return perfect_nbrs

def collatz_sequence(n):
    if n <= 0:
        raise ValueError("the number must be a positive integer")

    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq

def harshad_numbers_up_to(n):
    if n < 0:
        raise ValueError("the number must be positive")
    if n == 0:
        raise ValueError("the number must be greater than 0")

    harshad_nbrs = []
    for num in range(1, n+1):
        digit_sum = sum(int(d) for d in str(num))
        if num % digit_sum == 0:
            harshad_nbrs.append(num)
    return harshad_nbrs


def first_harshad_numbers(n):
    if n < 0:
        raise ValueError("the number must be positive")
    harshad_nbrs = []
    num = 1
    while len(harshad_nbrs) < n:
        digit_sum = sum(int(d) for d in str(num))
        if num % digit_sum == 0:
            harshad_nbrs.append(num)
        num += 1
    return harshad_nbrs

def hamming_numbers_up_to(n):
    if n < 1:
        raise ValueError("the number must be positive and greater than 0")

    hamming_nbrs = [1]
    i2 = i3 = i5 = 0

    while True:
        next_val = min(hamming_nbrs[i2]*2, hamming_nbrs[i3]*3, hamming_nbrs[i5]*5)
        if next_val > n:
            break
        hamming_nbrs.append(next_val)
        if next_val == hamming_nbrs[i2]*2:
            i2 += 1
        if next_val == hamming_nbrs[i3]*3:
            i3 += 1
        if next_val == hamming_nbrs[i5]*5:
            i5 += 1
    return hamming_nbrs


def first_hamming_numbers(n):
    if n < 1:
        raise ValueError("the number must be positive and greater than 0")

    hamming_nbrs = [1]
    i2 = i3 = i5 = 0

    while len(hamming_nbrs) < n:
        next_val = min(hamming_nbrs[i2]*2, hamming_nbrs[i3]*3, hamming_nbrs[i5]*5)
        hamming_nbrs.append(next_val)
        if next_val == hamming_nbrs[i2]*2:
            i2 += 1
        if next_val == hamming_nbrs[i3]*3:
            i3 += 1
        if next_val == hamming_nbrs[i5]*5:
            i5 += 1
    return hamming_nbrs

def mersenne_numbers_up_to(n):
    if n < 1:
        raise ValueError("Numărul trebuie să fie cel puțin 1")

    def is_prime(p):
        if p < 2:
            return False
        for i in range(2, int(p**0.5) + 1):
            if p % i == 0:
                return False
        return True

    mersenne_nbrs = []
    p = 2
    while True:
        m = 2**p - 1
        if m > n:
            break
        if is_prime(p):
            mersenne_nbrs.append(m)
        p += 1

    return mersenne_nbrs


def first_mersenne_numbers(count):
    if count < 1:
        raise ValueError("Count trebuie să fie cel puțin 1")

    def is_prime(p):
        if p < 2:
            return False
        for i in range(2, int(p**0.5) + 1):
            if p % i == 0:
                return False
        return True

    mersenne_nbrs = []
    p = 2
    while len(mersenne_nbrs) < count:
        if is_prime(p):
            mersenne_nbrs.append(2**p - 1)
        p += 1

    return mersenne_nbrs

def fermat_numbers_up_to(n):
    if n < 1:
        raise ValueError("Numărul trebuie să fie cel puțin 1")

    fermat_nbrs = []
    k = 0
    while True:
        f = 2**(2**k) + 1
        if f > n:
            break
        fermat_nbrs.append(f)
        k += 1

    return fermat_nbrs


def first_fermat_numbers(count):
    if count < 1:
        raise ValueError("Count trebuie să fie cel puțin 1")

    fermat_nbrs = []
    k = 0
    while len(fermat_nbrs) < count:
        fermat_nbrs.append(2**(2**k) + 1)
        k += 1

    return fermat_nbrs

def pell_numbers_up_to(n):
    if n < 0:
        raise ValueError("Numărul trebuie să fie cel puțin 0")

    pell_nbrs = [0, 1]
    while True:
        next_pell = 2 * pell_nbrs[-1] + pell_nbrs[-2]
        if next_pell > n:
            break
        pell_nbrs.append(next_pell)

    return [num for num in pell_nbrs if num <= n]


def first_pell_numbers(count):
    if count < 1:
        raise ValueError("Count trebuie să fie cel puțin 1")

    pell_nbrs = [0, 1]
    while len(pell_nbrs) < count:
        pell_nbrs.append(2 * pell_nbrs[-1] + pell_nbrs[-2])

    return pell_nbrs[:count]

def length_of_sequence(seq):
    lg=0
    for i in seq:
        lg+=1
    return lg

def add_sequences(seq1, seq2):
    lg1=length_of_sequence(seq1)
    lg2=length_of_sequence(seq2)
    if lg1!=lg2:
        raise ValueError("length of sequences must be the same")
    s=[]
    for i in range(lg1):
        s.append(seq1[i]+seq2[i])
    return s

def subtract_sequences(seq1, seq2):
    lg1=length_of_sequence(seq1)
    lg2=length_of_sequence(seq2)
    if lg1!=lg2:
        raise ValueError("length of sequences must be the same")
    s=[]
    for i in range(lg1):
        s.append(seq1[i]-seq2[i])
    return s

def multiply_sequences(seq1, seq2):
    lg1=length_of_sequence(seq1)
    lg2=length_of_sequence(seq2)
    if lg1!=lg2:
        raise ValueError("length of sequences must be the same")
    m=[]
    for i in range(lg1):
        m.append(seq1[i]*seq2[i])
    return m

def divide_sequences(seq1, seq2):
    lg1=length_of_sequence(seq1)
    lg2=length_of_sequence(seq2)
    if lg1!=lg2:
        raise ValueError("length of sequences must be the same")
    d=[]
    for i in range(lg1):
        d.append(seq1[i]/seq2[i])
    return d

def modulo_sequences(seq1, seq2):
    lg1=length_of_sequence(seq1)
    lg2=length_of_sequence(seq2)
    if lg1!=lg2:
        raise ValueError("length of sequences must be the same")
    m=[]
    for i in range(lg1):
        m.append(seq1[i]%seq2[i])
    return m

def power_sequences(seq1, seq2):
    lg1=length_of_sequence(seq1)
    lg2=length_of_sequence(seq2)
    if lg1!=lg2:
        raise ValueError("length of sequences must be the same")
    p=[]
    for i in range(lg1):
        p.append(seq1[i]**seq2[i])
    return p

def absolute_difference_sequences(seq1, seq2):
    lg1=length_of_sequence(seq1)
    lg2=length_of_sequence(seq2)
    if lg1!=lg2:
        raise ValueError("length of sequences must be the same")
    ad=[]
    for i in range(lg1):
        diff=seq1[i]-seq2[i]
        if diff>=0:
            ad.append(diff)
        else:
            ad.append(-diff)
    return ad

def concat_sequences(seq1, seq2):
    return seq1+seq2

def logic_AND_on_sequences(seq1, seq2):
    lg1=length_of_sequence(seq1)
    lg2=length_of_sequence(seq2)
    if lg1!=lg2:
        raise ValueError("length of sequences must be the same")
    for i in range(lg1):
        if seq1[i]==0 or seq1[i]==1:
            if seq2[i]==0 or seq2[i]==1:
                pass
            else:
                raise ValueError("all values must be boolean")
    _and=[]
    for i in range(lg1):
        _and.append(seq1[i] and seq2[i])
    return _and

def logic_OR_on_sequences(seq1, seq2):
    lg1=length_of_sequence(seq1)
    lg2=length_of_sequence(seq2)
    if lg1!=lg2:
        raise ValueError("length of sequences must be the same")
    for i in range(lg1):
        if seq1[i]==0 or seq1[i]==1:
            if seq2[i]==0 or seq2[i]==1:
                pass
            else:
                raise ValueError("all values must be boolean")
    _or=[]
    for i in range(lg1):
        _or.append(seq1[i] or seq2[i])
    return _or

def logic_XOR_on_sequences(seq1, seq2):
    lg1=length_of_sequence(seq1)
    lg2=length_of_sequence(seq2)
    if lg1!=lg2:
        raise ValueError("length of sequences must be the same")
    for i in range(lg1):
        if seq1[i]==0 or seq1[i]==1:
            if seq2[i]==0 or seq2[i]==1:
                pass
            else:
                raise ValueError("all values must be boolean")
    _xor=[]
    for i in range(lg1):
        _xor.append(seq1[i] != seq2[i])
    return _xor

def sum_elements_of_sequence(seq):
    return sum(seq)

def max_from_sequence(seq):
    return max(seq)

def min_from_sequence(seq):
    return min(seq)

def arithmetic_mean(seq):
    lg=length_of_sequence(seq)
    s=sum_elements_of_sequence(seq)
    return s/lg

