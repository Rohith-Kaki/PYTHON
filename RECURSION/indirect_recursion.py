def even_number(n):
    if n == 0:
        return True
    else:
        return odd_number(n - 1)

def odd_number(n):
    if n == 0:
        return False
    else:
        return even_number(n - 1)

# Calling the indirect recursion functions
result_even = even_number(6)
result_odd = odd_number(5)

print("Is 6 an even number?", result_even)
print("Is 5 an odd number?", result_odd)
