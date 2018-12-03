# Enter your code here. Read input from STDIN. Print output to STDOUT
def median(sorted_list):
  l = len(sorted_list)
  if l%2 == 0:
    return (sorted_list[l // 2] + sorted_list[(l // 2) - 1]) / 2
  else:
    return float(sorted_list[l // 2])

num = int(input())
arr = list(map(int, input().split()))
freq = list(map(int, input().split()))

data_set = []
for n,f in zip(arr, freq):
  data_set.extend([n]*f)
data_set.sort()

size = len(data_set)
q1 = None
q3 = None

if size % 2 == 0:
  q1 = median(data_set[0:(size//2)])
  q3 = median(data_set[(size//2):])
else:
   q1 = median(data_set[0:(size//2)])
   q3 = median(data_set[((size//2) + 1):])

print(q3-q1)
