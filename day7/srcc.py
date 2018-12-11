# Enter your code here. Read input from STDIN. Print output to STDOUT
def rank(x):
  r = {}
  val = 1
  for num in sorted(x):
    r[num] = val
    val += 1
  return [r[i] for i in x]

  

def srcc(rx,ry):
  n = len(rx)
  square_differences = [(x-y)*(x-y) for x,y in zip(rx,ry)]
  
  numer = 6*sum(square_differences)
  denom = n**3 - n
  return (1-(numer/denom))


n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

print(round(srcc(rank(x),rank(y)),3))
