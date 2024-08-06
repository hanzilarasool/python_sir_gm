def right_angled_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)

right_angled_triangle(5)


# inverted triangle ,now 
def inverted_triangle(n):
    for i in range(n, 0, -1):
        print('*' * i)

inverted_triangle(5)

# pattern 

def find_divisible_numbers(start, end):
    divisible_numbers = [number for number in range(start, end + 1) if number % 7 == 0 and number % 5 == 0]
    return divisible_numbers

# Example usage:
start = 1
end = 100
result = find_divisible_numbers(start, end)
print("Numbers divisible by both 7 and 5:", result)

