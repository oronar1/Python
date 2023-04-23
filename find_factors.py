def find_factors(n):
    result = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            result.add[i]
            result.add[n//i]
    return list(result)
