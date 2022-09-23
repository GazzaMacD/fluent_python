# Keep list comprehensions to one line

symbols = "$¢£¥€¤"
codes = [ord(symbol) for symbol in symbols]
print(codes)

# Use list comprehensions for filtering when parent sequence
# Otherwise use generator expressions to save memory
# *Note the use of x in both, x is scoped and there is no masking
parent = (x for x in range(1000000))
div_by_tenthou = [x for x in parent if x % 10000 == 0]
print(div_by_tenthou)
