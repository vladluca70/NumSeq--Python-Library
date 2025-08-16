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

---

Enjoy generating number sequences with **NumSeq**! 🎉  
Contributions and suggestions are welcome. 🚀

