def generate_series(a: int):
    # if even, reduce by 1
    n = a if a % 2 != 0 else a - 1  
    series = [2 * i + 1 for i in range(n)]  # first n odd numbers
    return series


# Example usage:
a = int(input("Enter a number: "))
result = generate_series(a)
print("Output:", ", ".join(map(str, result)))
