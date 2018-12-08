# Enter your code here. Read input from STDIN. Print output to STDOUT
import operator as op
from functools import reduce

## Used this code from: https://stackoverflow.com/a/4941932
def nCr(n,r):
  r = min(r, n-r)
  numer = reduce(op.mul, range(n, n-r, -1), 1)
  denom = reduce(op.mul, range(1, r+1), 1)
  return numer//denom

p_b = round((1.09 / (1 + 1.09)), 3)
p_g = round((1 / (1 + 1.09)), 3)

answer = 0.0
n = 6
for i in range(3,7):
  answer += round(nCr(n,i)*(p_b**i)*(p_g**(n-i)), 3)

print(answer)
