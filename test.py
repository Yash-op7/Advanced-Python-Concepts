set_a: set[int] = {1, 2, 3, 4, 5}
set_b: set[int] = {4, 5, 6, 7, 8}

print("Set union", set_a | set_b)
print("Set difference", set_a - set_b)
print("Set intersection", set_a & set_b)
print("Unique elements or Symmetric difference or A⋃B - A⋂B", set_a ^ set_b)