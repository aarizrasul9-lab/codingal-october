result = 4 ** 3   # 4 raised to the power of 3
print(result)
result = pow(4, 3)           # 4^3 = 64
result = pow(4, 3, 5)
import math
result = math.pow(4, 3)      # 64.0
def power_calc(base, exponent):
    return base ** exponent  # or pow(base, exponent)

print(power_calc(2, 5))  # Output: 32