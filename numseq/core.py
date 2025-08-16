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