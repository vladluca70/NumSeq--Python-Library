import math

def naturals0(n):
    first_n_naturals=[]
    for i in range(n+1):
        first_n_naturals.append(i)
    return first_n_naturals

def naturals(n):
    first_n_naturals=[]
    for i in range(1,n+1):
        first_n_naturals.append(i)
    return first_n_naturals

def odd_numbers_up_to(n):
    odds=[]
    for i in range(1,n+1,2):
        odds.append(i)
    return odds

def first_odd_numbers(n):
    first_odds=[]
    for i in range(0,n):
        first_odds.append(i*2+1)
    return first_odds

def even_numbers_up_to(n):
    odds=[]
    for i in range(0,n,2):
        odds.append(i)
    return odds

def first_even_numbers(n):
    first_odds=[]
    for i in range(0,n):
        first_odds.append(i*2)
    return first_odds

def perfect_squares_up_to(n):
    perfect_squares=[]
    last=int(math.sqrt(n))
    for i in range (last+1):
        perfect_squares.append(i*i)
    return perfect_squares

def first_perfect_square_numbers(n):
    first_perfect_sqrt_numbers=[]
    for i in range(n):
        first_perfect_sqrt_numbers.append(i*i)
    return first_perfect_sqrt_numbers

def perfect_cubes_up_to(n):
    perfect_cubes=[]
    last=int(math.cbrt(n))
    for i in range (last+1):
        perfect_cubes.append(i**3)
    return perfect_cubes

def first_perfect_cube_numbers(n):
    first_perf_cube_numbers=[]
    for i in range(n):
        first_perf_cube_numbers.append(i**3)
    return first_perf_cube_numbers