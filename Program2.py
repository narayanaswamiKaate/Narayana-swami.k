def generate_series(a: int):
    series = []
    for i in range(a):
        series.append(2 * i + 1)   # formula for odd numbers
    return series


# Example usage:
a = int(input("Enter a number: "))
result = generate_series(a)
print("Output:", ", ".join(map(str, result)))
