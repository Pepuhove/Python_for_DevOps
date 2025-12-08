import sys

# you can use start,stop,step arguments in range function
numbers_list = list(range(1_000_000))
numbers_range = range(1_000_000)


list_mb = sys.getsizeof(numbers_list) / (1024**2)
range_mb = sys.getsizeof(numbers_range) / (1024**2)

print(f"Memory size of list in mb: {list_mb:.2f} bytes")
print(f"Memory size of range in mb: {range_mb:.6f} bytes")