# NumSeq - Python Library 🧮

**NumSeq** is a Python library that generates well-known number sequences.  
It provides simple and efficient functions for creating sequences like natural numbers, odd numbers, and many classical mathematical sequences. Some of the sequences you can generate include:

- **Perfect squares** and **perfect cubes**  
- **Triangular numbers** and **tetrahedral numbers**  
- **Fibonacci** and **Tribonacci numbers**  
- **Lucas numbers**  
- **Catalan numbers**  
- **Padovan** and **Perrin numbers**  
- **Motzkin numbers**  
- **Armstrong numbers**  
- **Perfect numbers**  
- **Collatz sequence**  
- **Harshad numbers**  
- **Hamming numbers**  
- **Mersenne** and **Fermat numbers**  
- **Pell numbers**

Each function is designed to be intuitive, with clear parameters and return values, allowing you to quickly generate sequences for learning, testing, or computational purposes.


You can find the library and install it from [PyPI](https://pypi.org/project/numseq/0.1.1/).

---

## Available Functions

### 1. `naturals0(n)` 🌱  
- **Description:** Returns the first `n+1` natural numbers starting from 0.  
- **Parameter:**  
  - `n` (int) – the number up to which the sequence is generated (inclusive). Must be a positive number.  
- **Returns:**  
  - List of integers `[0, 1, 2, ..., n]`.  
- **Example:**  
```python
naturals0(5)  # returns [0, 1, 2, 3, 4, 5]
```

### 2. `naturals(n)` 🌿  
- **Description:** Returns the first `n` natural numbers starting from 1.  
- **Parameter:**  
  - `n` (int) – the number of natural numbers to generate. Must be a positive number.  
- **Returns:**  
  - List of integers `[1, 2, 3, ..., n]`.  
- **Example:**  
```python
naturals(5)  # returns [1, 2, 3, 4, 5]
```

### 3. `odd_numbers_up_to(n)` 🔢  
- **Description:** Returns all odd numbers from 1 up to `n` (inclusive if `n` is odd).  
- **Parameter:**  
  - `n` (int) – the upper limit for generating odd numbers. Must be a positive number.  
- **Returns:**  
  - List of odd numbers `[1, 3, 5, ..., ≤ n]`.  
- **Example:**  
```python
odd_numbers_up_to(10)  # returns [1, 3, 5, 7, 9]
```

### 4. `first_odd_numbers(n)` 🌟  
- **Description:** Returns the first `n` odd numbers.  
- **Parameter:**  
  - `n` (int) – the number of odd numbers to generate. Must be a positive number.  
- **Returns:**  
  - List of the first `n` odd numbers `[1, 3, 5, ..., (2*n-1)]`.  
- **Example:**  
```python
first_odd_numbers(5)  # returns [1, 3, 5, 7, 9]
```

### 5. `even_numbers_up_to(n)` ⚡  
- **Description:** Returns all even numbers from 0 up to `n` (exclusive).  
- **Parameter:**  
  - `n` (int) – the upper limit for generating even numbers. Must be a positive number.  
- **Returns:**  
  - List of even numbers `[0, 2, 4, ..., < n]`.  
- **Example:**  
```python
even_numbers_up_to(10)  # returns [0, 2, 4, 6, 8]
```

### 6. `first_even_numbers(n)` 💧  
- **Description:** Returns the first `n` even numbers starting from 0.  
- **Parameter:**  
  - `n` (int) – the number of even numbers to generate. Must be a positive number.  
- **Returns:**  
  - List of the first `n` even numbers `[0, 2, 4, ..., 2*(n-1)]`.  
- **Example:**  
```python
first_even_numbers(5)  # returns [0, 2, 4, 6, 8]
```

### 7. `perfect_squares_up_to(n)` 🔲  
- **Description:** Returns all perfect square numbers less than or equal to `n`.  
- **Parameter:**  
  - `n` (int) – the upper limit for generating perfect squares. Must be a positive number.  
- **Returns:**  
  - List of perfect squares `[0, 1, 4, 9, ..., ≤ n]`.  
- **Example:**  
```python
perfect_squares_up_to(10)  # returns [0, 1, 4, 9]
```

### 8. `first_perfect_square_numbers(n)` ✨  
- **Description:** Returns the first `n` perfect square numbers starting from 0.  
- **Parameter:**  
  - `n` (int) – the number of perfect squares to generate. Must be a positive number.  
- **Returns:**  
  - List of the first `n` perfect squares `[0, 1, 4, 9, ..., (n-1)^2]`.  
- **Example:**  
```python
first_perfect_square_numbers(5)  # returns [0, 1, 4, 9, 16]
```

### 9. `perfect_cubes_up_to(n)` 🟫  
- **Description:** Returns all perfect cube numbers less than or equal to `n`.  
- **Parameter:**  
  - `n` (int) – the upper limit for generating perfect cubes. Must be a positive number.  
- **Returns:**  
  - List of perfect cubes `[0, 1, 8, 27, ..., ≤ n]`.  
- **Example:**  
```python
perfect_cubes_up_to(30)  # returns [0, 1, 8, 27]
```

### 10. `first_perfect_cube_numbers(n)` 🔹  
- **Description:** Returns the first `n` perfect cube numbers starting from 0.  
- **Parameter:**  
  - `n` (int) – the number of perfect cubes to generate. Must be a positive number.  
- **Returns:**  
  - List of the first `n` perfect cubes `[0, 1, 8, 27, ..., (n-1)^3]`.  
- **Example:**  
```python
first_perfect_cube_numbers(5)  # returns [0, 1, 8, 27, 64]
```

### 11. `triangular_numbers_up_to(n)` 🔺  
- **Description:** Returns all triangular numbers less than or equal to `n`.  
- **Formula:** `T_k = k * (k + 1) / 2`, where `T_k` is the k-th triangular number.  
- **Parameter:**  
  - `n` (int) – the upper limit for generating triangular numbers. Must be a positive number.  
- **Returns:**  
  - List of triangular numbers `[1, 3, 6, 10, ..., ≤ n]`.  
- **Example:**  
```python
triangular_numbers_up_to(15)  # returns [1, 3, 6, 10, 15]
```

### 12. `first_triangular_numbers(n)` 🔹  
- **Description:** Returns the first `n` triangular numbers starting from 1.  
- **Formula:** `T_k = k * (k + 1) / 2`  
- **Parameter:**  
  - `n` (int) – the number of triangular numbers to generate. Must be a positive number.  
- **Returns:**  
  - List of the first `n` triangular numbers `[1, 3, 6, 10, ..., T_n]`.  
- **Example:**  
```python
first_triangular_numbers(5)  # returns [1, 3, 6, 10, 15]
```

### 13. `tetrahedral_numbers_up_to(n)` 🔷  
- **Description:** Returns all tetrahedral numbers less than or equal to `n`.  
- **Formula:** `Te_k = k * (k + 1) * (k + 2) / 6`, where `Te_k` is the k-th tetrahedral number.  
- **Parameter:**  
  - `n` (int) – the upper limit for generating tetrahedral numbers. Must be a positive number.  
- **Returns:**  
  - List of tetrahedral numbers `[1, 4, 10, 20, ..., ≤ n]`.  
- **Example:**  
```python
tetrahedral_numbers_up_to(20)  # returns [1, 4, 10, 20]
```

### 14. `first_tetrahedral_numbers(n)` 🔹  
- **Description:** Returns the first `n` tetrahedral numbers starting from 1.  
- **Formula:** `Te_k = k * (k + 1) * (k + 2) / 6`  
- **Parameter:**  
  - `n` (int) – the number of tetrahedral numbers to generate. Must be a positive number.  
- **Returns:**  
  - List of the first `n` tetrahedral numbers `[1, 4, 10, 20, ..., Te_n]`.  
- **Example:**  
```python
first_tetrahedral_numbers(5)  # returns [1, 4, 10, 20, 35]
```

### 15. `prime_numbers_up_to(n)` 🥇  
- **Description:** Returns all prime numbers less than or equal to `n`.  
- **Parameter:**  
  - `n` (int) – the upper limit for generating prime numbers. Must be a positive number.  
- **Returns:**  
  - List of prime numbers `[2, 3, 5, 7, ..., ≤ n]`.  
- **Example:**  
```python
prime_numbers_up_to(10)  # returns [2, 3, 5, 7]
```

### 16. `first_prime_numbers(n)` 🔢  
- **Description:** Returns the first `n` prime numbers starting from 2.  
- **Parameter:**  
  - `n` (int) – the number of prime numbers to generate. Must be a positive number.  
- **Returns:**  
  - List of the first `n` prime numbers `[2, 3, 5, 7, ..., P_n]`.  
- **Example:**  
```python
first_prime_numbers(5)  # returns [2, 3, 5, 7, 11]
```

### 17. `fibonacci_numbers_up_to(n)` 🌊  
- **Description:** Returns all Fibonacci numbers less than or equal to `n`.  
- **Parameter:**  
  - `n` (int) – the upper limit for generating Fibonacci numbers. Must be a positive number.  
- **Returns:**  
  - List of Fibonacci numbers `[0, 1, 1, 2, 3, 5, 8, ..., ≤ n]`.  
- **Fibonacci numbers formula:**  

$$
F_0 = 0, \quad F_1 = 1, \quad F_n = F_{n-1} + F_{n-2}, \quad n \ge 2
$$

- **Example:**  
```python
fibonacci_numbers_up_to(10)  # returns [0, 1, 1, 2, 3, 5, 8]
```

### 18. `first_fibonacci_numbers(n)` 🔢  
- **Description:** Returns the first `n` Fibonacci numbers.  
- **Parameter:**  
  - `n` (int) – the number of Fibonacci numbers to generate. Must be greater than 1.  
- **Returns:**  
  - List of the first `n` Fibonacci numbers `[0, 1, 1, 2, 3, 5, ...]`.  
- **Fibonacci numbers formula:**  

$$
F_0 = 0, \quad F_1 = 1, \quad F_n = F_{n-1} + F_{n-2}, \quad n \ge 2
$$

- **Example:**  
```python
first_fibonacci_numbers(7)  # returns [0, 1, 1, 2, 3, 5, 8]
```

### 19. `lucas_numbers_up_to(n)` 🌟  
- **Description:** Returns all Lucas numbers less than or equal to `n`.  
- **Parameter:**  
  - `n` (int) – the upper limit for generating Lucas numbers. Must be a positive number.  
- **Returns:**  
  - List of Lucas numbers `[2, 1, 3, 4, 7, 11, 18, ..., ≤ n]`.  
- **Lucas numbers formula:**  

$$
L_0 = 2, \quad L_1 = 1, \quad L_n = L_{n-1} + L_{n-2}, \quad n \ge 2
$$

- **Example:**  
```python
lucas_numbers_up_to(20)  # returns [2, 1, 3, 4, 7, 11, 18]
```

### 20. `first_lucas_numbers(n)` 🔢  
- **Description:** Returns the first `n` Lucas numbers.  
- **Parameter:**  
  - `n` (int) – the number of Lucas numbers to generate. Must be greater than 1.  
- **Returns:**  
  - List of the first `n` Lucas numbers `[2, 1, 3, 4, 7, 11, ...]`.  
- **Lucas numbers formula:**  

$$
L_0 = 2, \quad L_1 = 1, \quad L_n = L_{n-1} + L_{n-2}, \quad n \ge 2
$$

- **Example:**  
```python
first_lucas_numbers(7)  # returns [2, 1, 3, 4, 7, 11, 18]
```
### 21. `catalan_numbers_up_to(n)` 🧮  
- **Description:** Returns all Catalan numbers less than or equal to `n`.  
- **Parameter:**  
  - `n` (int) – the upper limit for generating Catalan numbers. Must be a positive number.  
- **Returns:**  
  - List of Catalan numbers `[1, 1, 2, 5, 14, 42, ..., ≤ n]`.  
- **Catalan numbers formula:**  

$$
C_n = \frac{(2n)!}{(n+1)! * n!}, \quad n \ge 0
$$

- **Example:**  
```python
catalan_numbers_up_to(20)  # returns [1, 1, 2, 5, 14]
```

### 22. `first_catalan_numbers(n)` 🔢  
- **Description:** Returns the first `n` Catalan numbers.  
- **Parameter:**  
  - `n` (int) – the number of Catalan numbers to generate. Must be a positive number.  
- **Returns:**  
  - List of the first `n` Catalan numbers `[1, 1, 2, 5, 14, ...]`.  
- **Catalan numbers formula:**  

$$
C_n = \frac{(2n)!}{(n+1)! * n!}, \quad n \ge 0
$$

- **Example:**  
```python
first_catalan_numbers(7)  # returns [1, 1, 2, 5, 14, 42, 132]
```

### 23. `factorial_numbers_up_to(n)`  🔢  
- **Description:** Returns all factorial numbers less than or equal to `n`.  
- **Parameter:**  
  - `n` (int) – the maximum value up to which factorial numbers are generated. Must be a positive number.  
- **Returns:**  
  - List of factorial numbers `[1, 2, 6, 24, ...]` that are less than or equal to `n`.  
- **Example:**  
```python
factorial_numbers_up_to(30)  # returns [1, 2, 6, 24]
```

### 24. `first_factorial_numbers(n)` 🔢  
- **Description:** Returns the first `n` factorial numbers.  
- **Parameter:**  
  - `n` (int) – the number of factorial numbers to generate. Must be a positive number.  
- **Returns:**  
  - List of the first `n` factorial numbers `[1, 1, 2, 6, 24, ...]`.  
- **Factorial numbers formula:**  

$$
n! = 1 \cdot 2 \cdot 3 \cdot \dots \cdot n, \quad n \ge 0
$$

- **Example:**  
```python
first_factorial_numbers(7)  # returns [1, 1, 2, 6, 24, 120, 720]
```

### 25.`padovan_numbers_up_to(n)` 🔢  
- **Description:** Returns all Padovan numbers less than or equal to `n`.  
- **Parameter:**  
  - `n` (int) – the maximum value for Padovan numbers. Must be a positive number greater than 0.  
- **Returns:**  
  - List of Padovan numbers `[1, 1, 1, 2, 2, 3, 4, 5, 7, ...]` up to `n`.  
- **Padovan numbers formula (recurrence relation):**  

$$
P(n) = P(n-2) + P(n-3), \quad P(0)=P(1)=P(2)=1, \quad n \ge 0
$$

- **Example:**  
```python
padovan_numbers_up_to(10)  # returns [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
```

### 26.`first_padovan_numbers(n)` 🔢  
- **Description:** Returns the first `n` Padovan numbers.  
- **Parameter:**  
  - `n` (int) – the number of Padovan numbers to generate. Must be a positive number.  
- **Returns:**  
  - List of the first `n` Padovan numbers `[1, 1, 1, 2, 2, 3, 4, 5, 7, ...]`.  
- **Padovan numbers formula (recurrence relation):**  

$$
P(n) = P(n-2) + P(n-3), \quad P(0)=P(1)=P(2)=1, \quad n \ge 0
$$

- **Example:**  
```python
first_padovan_numbers(10)  # returns [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
```

### 27. `perrin_numbers_up_to(n)` 🔢  
- **Description:** Returns all Perrin numbers less than or equal to `n`.  
- **Parameter:**  
  - `n` (int) – the maximum value for Perrin numbers. Must be a positive number greater than 0.  
- **Returns:**  
  - List of Perrin numbers `[3, 0, 2, 3, 2, 5, 5, 7, 10, ...]` up to `n`.  
- **Perrin numbers formula (recurrence relation):**  

$$
P(n) = P(n-2) + P(n-3), \quad P(0)=3, P(1)=0, P(2)=2, \quad n \ge 0
$$

- **Example:**  
```python
perrin_numbers_up_to(10)  # returns [3, 0, 2, 3, 2, 5, 5, 7, 10]
```

### 28. `first_perrin_numbers(n)` 🔢  
- **Description:** Returns the first `n` Perrin numbers.  
- **Parameter:**  
  - `n` (int) – the number of Perrin numbers to generate. Must be a positive number.  
- **Returns:**  
  - List of the first `n` Perrin numbers `[3, 0, 2, 3, 2, 5, 5, 7, 10, ...]`.  
- **Perrin numbers formula (recurrence relation):**  

$$
P(n) = P(n-2) + P(n-3), \quad P(0)=3, P(1)=0, P(2)=2, \quad n \ge 0
$$

- **Example:**  
```python
first_perrin_numbers(10)  # returns [3, 0, 2, 3, 2, 5, 5, 7, 10, 12]
```

### 29. `motzkin_numbers_up_to(n)` 🔢  
- **Description:** Returns all Motzkin numbers less than or equal to `n`.  
- **Parameter:**  
  - `n` (int) – the upper limit for Motzkin numbers. Must be a positive number.  
- **Returns:**  
  - List of all Motzkin numbers ≤ `n` `[1, 1, 2, 4, 9, ...]`.  
- **Motzkin numbers formula (recurrence relation):**  

$$
M(n) = M(n-1) + \sum_{k=0}^{n-2} M(k) \cdot M(n-2-k), \quad M(0)=1, M(1)=1, \quad n \ge 2
$$

- **Example:**  
```python
motzkin_numbers_up_to(20)  # returns [1, 1, 2, 4, 9]
```

### 30. `first_motzkin_numbers(n)` 🔢  
- **Description:** Returns the first `n` Motzkin numbers.  
- **Parameter:**  
  - `n` (int) – the number of Motzkin numbers to generate. Must be a positive number.  
- **Returns:**  
  - List of the first `n` Motzkin numbers `[1, 1, 2, 4, 9, 21, ...]`.  
- **Motzkin numbers formula (recurrence relation):**  

$$
M(n) = M(n-1) + \sum_{k=0}^{n-2} M(k) \cdot M(n-2-k), \quad M(0)=1, M(1)=1, \quad n \ge 2
$$

- **Example:**  
```python
first_motzkin_numbers(7)  # returns [1, 1, 2, 4, 9, 21, 51]
```

### 31. `tribonacci_numbers_up_to(n)` 🔢  
- **Description:** Returns all Tribonacci numbers less than or equal to `n`.  
- **Parameter:**  
  - `n` (int) – the upper limit for Tribonacci numbers. Must be a positive number.  
- **Returns:**  
  - List of Tribonacci numbers `[0, 1, 1, 2, 4, 7, ...]` that do not exceed `n`.  
- **Tribonacci numbers formula (recurrence relation):**  

$$
T(n) = T(n-1) + T(n-2) + T(n-3), \quad T(0)=0, T(1)=1, T(2)=1, \quad n \ge 3
$$

- **Example:**  
```python
tribonacci_numbers_up_to(20)  # returns [0, 1, 1, 2, 4, 7, 13]
```

### 32. `first_tribonacci_numbers(n)` 🔢  
- **Description:** Returns the first `n` Tribonacci numbers.  
- **Parameter:**  
  - `n` (int) – the number of Tribonacci numbers to generate. Must be a positive number.  
- **Returns:**  
  - List of the first `n` Tribonacci numbers `[0, 1, 1, 2, 4, 7, ...]`.  
- **Tribonacci numbers formula (recurrence relation):**  

$$
T(n) = T(n-1) + T(n-2) + T(n-3), \quad T(0)=0, T(1)=1, T(2)=1, \quad n \ge 3
$$

- **Example:**  
```python
first_tribonacci_numbers(7)  # returns [0, 1, 1, 2, 4, 7, 13]
```

### 33. `armstrong_numbers_up_to(n)` 🔢  
- **Description:** Returns all Armstrong numbers less than or equal to `n`.  
- **Parameter:**  
  - `n` (int) – the upper limit for Armstrong numbers. Must be a positive number.  
- **Returns:**  
  - List of Armstrong numbers `[1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, ...]` that do not exceed `n`.  
- **Armstrong number formula:**  

A number is an Armstrong number if:

$$
N = \sum_{i=1}^{k} d_i^k
$$

where \(d_i\) are the digits of \(N\) and \(k\) is the number of digits in \(N\).  

- **Example:**  
```python
armstrong_numbers_up_to(500)  # returns [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
```


### 34. `first_armstrong_numbers(n)` 🔢  
- **Description:** Returns the first `n` Armstrong numbers in order.  
- **Parameter:**  
  - `n` (int) – the number of Armstrong numbers to generate. Must be a positive number.  
- **Returns:**  
  - List of the first `n` Armstrong numbers `[1, 2, 3, 4, 5, ...]`.  
- **Armstrong number formula:**  

A number is an Armstrong number if:

$$
N = \sum_{i=1}^{k} d_i^k
$$

where \(d_i\) are the digits of \(N\) and \(k\) is the number of digits in \(N\).  

- **Example:**  
```python
first_armstrong_numbers(10)  # returns [1, 2, 3, 4, 5, 6, 7, 8, 9, 153]
```

### 35. `perfect_numbers_up_to(n)` 🔢  
- **Description:** Returns all perfect numbers less than or equal to `n`.  
- **Parameter:**  
  - `n` (int) – the upper limit to generate perfect numbers. Must be a positive number.  
- **Returns:**  
  - List of perfect numbers `≤ n` `[6, 28, 496, ...]`.  
- **Perfect number formula:**  

A number \(N\) is perfect if:

$$
N = \sum_{d | N, d < N} d
$$

i.e., the sum of its proper divisors equals the number itself.  

- **Example:**  
```python
perfect_numbers_up_to(500)  # returns [6, 28, 496]
```

### 36. `first_perfect_numbers(n)` 🔢  
- **Description:** Returns the first `n` perfect numbers in order.  
- **Parameter:**  
  - `n` (int) – the number of perfect numbers to generate. Must be a positive number.  
- **Returns:**  
  - List of the first `n` perfect numbers `[6, 28, 496, ...]`.  
- **Perfect number formula:**  

A number \(N\) is perfect if:

$$
N = \sum_{d | N, d < N} d
$$

i.e., the sum of its proper divisors equals the number itself.  

- **Example:**  
```python
first_perfect_numbers(4)  # returns [6, 28, 496, 8128]
```

### 37. `collatz_sequence(n)` 🔢  
- **Description:** Generates the Collatz sequence starting from a positive integer `n`.  
- **Parameter:**  
  - `n` (int) – the starting number of the sequence. Must be a positive integer.  
- **Returns:**  
  - List of integers representing the Collatz sequence until it reaches 1.  

- **Collatz rules:**  
  1. Start with any positive integer `n`.  
  2. If `n` is even, divide it by 2.  
  3. If `n` is odd, multiply by 3 and add 1.  
  4. Repeat until `n` becomes 1.  

- **Example:**  
```python
collatz_sequence(6)  # returns [6, 3, 10, 5, 16, 8, 4, 2, 1]
```

### 38. `harshad_numbers_up_to(n)` 🔢  
- **Description:** Returns all Harshad (Niven) numbers less than or equal to `n`. A number is Harshad if it is divisible by the sum of its digits.  
- **Parameter:**  
  - `n` (int) – the upper limit to generate Harshad numbers. Must be a positive number.  
- **Returns:**  
  - List of Harshad numbers `≤ n` `[1, 2, 3, 4, 5, ...]`.  
- **Definition:**  
A number \(N\) is a Harshad number if:

$$
N \bmod S(N) = 0
$$

where \(S(N)\) is the sum of the digits of \(N\).  
- **Example:**  
```python
harshad_numbers_up_to(20)  # returns [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18]
```

### 39. `first_harshad_numbers(n)` 🔢  
- **Description:** Returns the first `n` Harshad (Niven) numbers in order. A number is Harshad if it is divisible by the sum of its digits.  
- **Parameter:**  
  - `n` (int) – the number of Harshad numbers to generate. Must be a positive number.  
- **Returns:**  
  - List of the first `n` Harshad numbers `[1, 2, 3, 4, 5, ...]`.  
- **Definition:**  
A number \(N\) is a Harshad number if:

$$
N \bmod S(N) = 0
$$

where \(S(N)\) is the sum of the digits of \(N\).  
- **Example:**  
```python
first_harshad_numbers(15)  # returns [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24]
```

### 40. `hamming_numbers_up_to(n)` 🔢  
- **Description:** Returns all Hamming numbers less than or equal to `n`. A Hamming number is a number whose only prime factors are 2, 3, or 5.  
- **Parameter:**  
  - `n` (int) – the upper limit to generate Hamming numbers. Must be a positive number greater than 0.  
- **Returns:**  
  - List of Hamming numbers `≤ n` `[1, 2, 3, 4, 5, 6, 8, ...]`.  
- **Definition:**  
A number \(N\) is a Hamming number if it can be expressed as:

$$
N = 2^i \cdot 3^j \cdot 5^k
$$

for non-negative integers \(i, j, k\).  
- **Example:**  
```python
hamming_numbers_up_to(20)  # returns [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16]
```

### 41. `first_hamming_numbers(n)` 🔢  
- **Description:** Returns the first `n` Hamming numbers in order. A Hamming number is a number whose only prime factors are 2, 3, or 5.  
- **Parameter:**  
  - `n` (int) – the number of Hamming numbers to generate. Must be a positive number greater than 0.  
- **Returns:**  
  - List of the first `n` Hamming numbers `[1, 2, 3, 4, 5, 6, 8, ...]`.  
- **Definition:**  
A number \(N\) is a Hamming number if it can be expressed as:

$$
N = 2^i \cdot 3^j \cdot 5^k
$$

for non-negative integers \(i, j, k\).  
- **Example:**  
```python
first_hamming_numbers(15)  # returns [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24]
```

### 42. `mersenne_numbers_up_to(n)` 🔢  
- **Description:** Returns all Mersenne numbers less than or equal to `n`. A Mersenne number is a number of the form \(2^p - 1\) where \(p\) is a prime number.  
- **Parameter:**  
  - `n` (int) – the upper limit to generate Mersenne numbers. Must be a positive number greater than 0.  
- **Returns:**  
  - List of Mersenne numbers `≤ n` `[3, 7, 31, ...]`.  
- **Definition:**  
A number \(M\) is a Mersenne number if it can be expressed as:

$$
M = 2^p - 1
$$

where \(p\) is prime.  
- **Example:**  
```python
mersenne_numbers_up_to(100)  # returns [3, 7, 31, 127]
```

### 43. `first_mersenne_numbers(count)` 🔢  
- **Description:** Returns the first `count` Mersenne numbers in order. A Mersenne number is a number of the form \(2^p - 1\) where \(p\) is a prime number.  
- **Parameter:**  
  - `count` (int) – the number of Mersenne numbers to generate. Must be a positive number greater than 0.  
- **Returns:**  
  - List of the first `count` Mersenne numbers `[3, 7, 31, ...]`.  
- **Definition:**  
A number \(M\) is a Mersenne number if it can be expressed as:

$$
M = 2^p - 1
$$

where \(p\) is prime.  
- **Example:**  
```python
first_mersenne_numbers(5)  # returns [3, 7, 31, 127, 8191]
```

### 44. `fermat_numbers_up_to(n)` 🔢  
- **Description:** Returns all Fermat numbers less than or equal to `n`. A Fermat number is a number of the form \(2^{2^k} + 1\).  
- **Parameter:**  
  - `n` (int) – the upper limit to generate Fermat numbers. Must be a positive number greater than 0.  
- **Returns:**  
  - List of Fermat numbers `≤ n` `[3, 5, 17, ...]`.  
- **Definition:**  
A number \(F\) is a Fermat number if it can be expressed as:

$$
F = 2^{2^k} + 1
$$

where \(k\) is a non-negative integer.  
- **Example:**  
```python
fermat_numbers_up_to(100)  # returns [3, 5, 17, 257]
```

### 45. `first_fermat_numbers(count)` 🔢  
- **Description:** Returns the first `count` Fermat numbers in order. A Fermat number is a number of the form \(2^{2^k} + 1\).  
- **Parameter:**  
  - `count` (int) – the number of Fermat numbers to generate. Must be a positive number greater than 0.  
- **Returns:**  
  - List of the first `count` Fermat numbers `[3, 5, 17, ...]`.  
- **Definition:**  
A number \(F\) is a Fermat number if it can be expressed as:

$$
F = 2^{2^k} + 1
$$

where \(k\) is a non-negative integer.  
- **Example:**  
```python
first_fermat_numbers(5)  # returns [3, 5, 17, 257, 65537]
```

### 46. `pell_numbers_up_to(n)` 🔢  
- **Description:** Returns all Pell numbers less than or equal to `n`. Pell numbers follow the recurrence \(P_n = 2P_{n-1} + P_{n-2}\) with initial values \(P_0 = 0\) and \(P_1 = 1\).  
- **Parameter:**  
  - `n` (int) – the upper limit. Must be a non-negative number.  
- **Returns:**  
  - List of all Pell numbers `≤ n` `[0, 1, 2, 5, 12, ...]`.  
- **Definition:**  
A number \(P_n\) is a Pell number if it satisfies:

$$
P_0 = 0, \quad P_1 = 1, \quad P_n = 2 \cdot P_{n-1} + P_{n-2} \quad \text{for } n \ge 2
$$

- **Example:**  
```python
pell_numbers_up_to(20)  # returns [0, 1, 2, 5, 12]
```

### 47. `first_pell_numbers(count)` 🔢  
- **Description:** Returns the first `count` Pell numbers in order. A Pell number is defined by the recurrence relation \(P_n = 2P_{n-1} + P_{n-2}\) with initial values \(P_0 = 0\) and \(P_1 = 1\).  
- **Parameter:**  
  - `count` (int) – the number of Pell numbers to generate. Must be a positive number greater than 0.  
- **Returns:**  
  - List of the first `count` Pell numbers `[0, 1, 2, 5, 12, ...]`.  
- **Definition:**  
A number \(P_n\) is a Pell number if it satisfies:

$$
P_0 = 0, \quad P_1 = 1, \quad P_n = 2 \cdot P_{n-1} + P_{n-2} \quad \text{for } n \ge 2
$$

- **Example:**  
```python
first_pell_numbers(6)  # returns [0, 1, 2, 5, 12, 29]
```

### 48. `add_sequences(seq1, seq2)` ➕  
- **Description:** Returns a new sequence that is the element-wise sum of two sequences of equal length.  
- **Parameters:**  
  - `seq1` (list of numbers) – the first sequence.  
  - `seq2` (list of numbers) – the second sequence. Must have the same length as `seq1`.  
- **Returns:**  
  - List of numbers representing the element-wise sum of `seq1` and `seq2`.  
- **Raises:**  
  - `ValueError` if the sequences are not of the same length.  
- **Example:**  
```python
add_sequences([1, 2, 3], [4, 5, 6])  # returns [5, 7, 9]
```

### 49. `subtract_sequences(seq1, seq2)` ➖  
- **Description:** Returns a new sequence that is the element-wise difference of two sequences of equal length.  
- **Parameters:**  
  - `seq1` (list of numbers) – the first sequence.  
  - `seq2` (list of numbers) – the second sequence. Must have the same length as `seq1`.  
- **Returns:**  
  - List of numbers representing the element-wise difference `seq1[i] - seq2[i]`.  
- **Raises:**  
  - `ValueError` if the sequences are not of the same length.  
- **Example:**  
```python
subtract_sequences([5, 7, 9], [1, 2, 3])  # returns [4, 5, 6]
```

### 50. `multiply_sequences(seq1, seq2)` ✖️  
- **Description:** Returns a new sequence that is the element-wise product of two sequences of equal length.  
- **Parameters:**  
  - `seq1` (list of numbers) – the first sequence.  
  - `seq2` (list of numbers) – the second sequence. Must have the same length as `seq1`.  
- **Returns:**  
  - List of numbers representing the element-wise product `seq1[i] * seq2[i]`.  
- **Raises:**  
  - `ValueError` if the sequences are not of the same length.  
- **Example:**  
```python
multiply_sequences([1, 2, 3], [4, 5, 6])  # returns [4, 10, 18]
```

### 51. `divide_sequences(seq1, seq2)` ➗  
- **Description:** Returns a new sequence that is the element-wise division of two sequences of equal length.  
- **Parameters:**  
  - `seq1` (list of numbers) – the numerator sequence.  
  - `seq2` (list of numbers) – the denominator sequence. Must have the same length as `seq1`.  
- **Returns:**  
  - List of numbers representing the element-wise division `seq1[i] / seq2[i]`.  
- **Raises:**  
  - `ValueError` if the sequences are not of the same length.  
  - `ZeroDivisionError` if any element in `seq2` is zero.  
- **Example:**  
```python
divide_sequences([4, 10, 18], [2, 5, 3])  # returns [2.0, 2.0, 6.0]
```

### 52. `modulo_sequences(seq1, seq2)` 🟰  
- **Description:** Returns a new sequence that is the element-wise modulo of two sequences of equal length.  
- **Parameters:**  
  - `seq1` (list of numbers) – the dividend sequence.  
  - `seq2` (list of numbers) – the divisor sequence. Must have the same length as `seq1`.  
- **Returns:**  
  - List of numbers representing the element-wise modulo `seq1[i] % seq2[i]`.  
- **Raises:**  
  - `ValueError` if the sequences are not of the same length.  
  - `ZeroDivisionError` if any element in `seq2` is zero.  
- **Example:**  
```python
modulo_sequences([5, 7, 10], [2, 3, 4])  # returns [1, 1, 2]
```

### 53. `power_sequences(seq1, seq2)` 🔺  
- **Description:** Returns a new sequence that is the element-wise exponentiation of two sequences of equal length.  
- **Parameters:**  
  - `seq1` (list of numbers) – the base sequence.  
  - `seq2` (list of numbers) – the exponent sequence. Must have the same length as `seq1`.  
- **Returns:**  
  - List of numbers representing the element-wise power `seq1[i] ** seq2[i]`.  
- **Raises:**  
  - `ValueError` if the sequences are not of the same length.  
- **Example:**  
```python
power_sequences([2, 3, 4], [3, 2, 1])  # returns [8, 9, 4]
```

### 54. `absolute_difference_sequences(seq1, seq2)` 🔹  
- **Description:** Returns a new sequence containing the element-wise absolute differences between two sequences of equal length.  
- **Parameters:**  
  - `seq1` (list of numbers) – the first sequence.  
  - `seq2` (list of numbers) – the second sequence. Must have the same length as `seq1`.  
- **Returns:**  
  - List of numbers representing the absolute differences `|seq1[i] - seq2[i]|`.  
- **Raises:**  
  - `ValueError` if the sequences are not of the same length.  
- **Example:**  
```python
absolute_difference_sequences([5, 7, 2], [3, 10, 2])  # returns [2, 3, 0]
```

### 55. `concat_sequences(seq1, seq2)` 🔗  
- **Description:** Returns a new sequence by concatenating two sequences end-to-end.  
- **Parameters:**  
  - `seq1` (list) – the first sequence.  
  - `seq2` (list) – the second sequence.  
- **Returns:**  
  - List containing all elements of `seq1` followed by all elements of `seq2`.  
- **Example:**  
```python
concat_sequences([1, 2, 3], [4, 5, 6])  # returns [1, 2, 3, 4, 5, 6]
```

### 56. `logic_AND_on_sequences(seq1, seq2)` 🔒  
- **Description:** Returns a new sequence containing the element-wise logical AND of two boolean sequences of equal length.  
- **Parameters:**  
  - `seq1` (list of 0 or 1) – the first boolean sequence.  
  - `seq2` (list of 0 or 1) – the second boolean sequence. Must have the same length as `seq1`.  
- **Returns:**  
  - List of numbers representing the logical AND of corresponding elements `seq1[i] and seq2[i]`.  
- **Raises:**  
  - `ValueError` if the sequences are not of the same length or contain non-boolean values.  
- **Example:**  
```python
logic_AND_on_sequences([1, 0, 1], [0, 1, 1])  # returns [0, 0, 1]
```

### 57. `logic_OR_on_sequences(seq1, seq2)` 🔓  
- **Description:** Returns a new sequence containing the element-wise logical OR of two boolean sequences of equal length.  
- **Parameters:**  
  - `seq1` (list of 0 or 1) – the first boolean sequence.  
  - `seq2` (list of 0 or 1) – the second boolean sequence. Must have the same length as `seq1`.  
- **Returns:**  
  - List of numbers representing the logical OR of corresponding elements `seq1[i] or seq2[i]`.  
- **Raises:**  
  - `ValueError` if the sequences are not of the same length or contain non-boolean values.  
- **Example:**  
```python
logic_OR_on_sequences([1, 0, 1], [0, 1, 1])  # returns [1, 1, 1]
```

### 58. `logic_XOR_on_sequences(seq1, seq2)` ✖️  
- **Description:** Returns a new sequence containing the element-wise logical XOR of two boolean sequences of equal length.  
- **Parameters:**  
  - `seq1` (list of 0 or 1) – the first boolean sequence.  
  - `seq2` (list of 0 or 1) – the second boolean sequence. Must have the same length as `seq1`.  
- **Returns:**  
  - List of numbers representing the logical XOR of corresponding elements `seq1[i] != seq2[i]`.  
- **Raises:**  
  - `ValueError` if the sequences are not of the same length or contain non-boolean values.  
- **Example:**  
```python
logic_XOR_on_sequences([1, 0, 1], [0, 1, 1])  # returns [1, 1, 0]
```

### 59. `sum_elements_of_sequence(seq)` ➕  
- **Description:** Returns the sum of all elements in a sequence.  
- **Parameter:**  
  - `seq` (list of numbers) – the sequence to sum.  
- **Returns:**  
  - Sum of all elements in the sequence.  
- **Example:**  
```python
sum_elements_of_sequence([1, 2, 3, 4])  # returns 10
```

### 60. `max_from_sequence(seq)` 📈  
- **Description:** Returns the maximum value from a sequence.  
- **Parameter:**  
  - `seq` (list of numbers) – the sequence to evaluate.  
- **Returns:**  
  - The largest number in the sequence.  
- **Example:**  
```python
max_from_sequence([1, 2, 3, 4])  # returns 4
```

### 61. `min_from_sequence(seq)` 📉  
- **Description:** Returns the minimum value from a sequence.  
- **Parameter:**  
  - `seq` (list of numbers) – the sequence to evaluate.  
- **Returns:**  
  - The smallest number in the sequence.  
- **Example:**  
```python
min_from_sequence([1, 2, 3, 4])  # returns 1
```

### 62. `arithmetic_mean(seq)` ➗  
- **Description:** Returns the arithmetic mean (average) of the elements in a sequence.  
- **Parameter:**  
  - `seq` (list of numbers) – the sequence to evaluate. Must contain at least one element.  
- **Returns:**  
  - The arithmetic mean of the sequence.  
- **Example:**  
```python
arithmetic_mean([2, 4, 6, 8])  # returns 5.0
```

---

Enjoy generating number sequences with **NumSeq**! 🎉  
Contributions and suggestions are welcome. 🚀

