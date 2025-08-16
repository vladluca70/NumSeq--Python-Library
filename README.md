# NumSeq - Python Library 🧮

**NumSeq** is a Python library that generates well-known number sequences.  
It provides simple and efficient functions for creating sequences like natural numbers, odd numbers, and other useful numeric sequences for programming or math.

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

---

Enjoy generating number sequences with **NumSeq**! 🎉  
Contributions and suggestions are welcome. 🚀

