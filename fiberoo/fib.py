def the_fibsteroo(n):
    """Calculates the fibonacci sequence non-recursively:
    
    Args:
        n: the Fibonacci number you want
        
    Returns:
        the nth Fibonacci number
    """
    cases = [0, 1]
    for i in range(2, n + 1):
        cases.append(cases[i-1] + cases[i-2])
    return cases[n]