from decimal import *
import math
d = Decimal(input())
temp = d.exp() + d.ln() + d.log10() + d.sqrt()
print(temp)
