# Enter your code here. Read input from STDIN. Print output to STDOUT
def median(sorted_list):
  l = len(sorted_list)
  if l%2 == 0:
    return (sorted_list[l // 2] + sorted_list[(l // 2) - 1]) // 2 #as it is guranteed the median will be integer
  else:
    return sorted_list[l // 2]

num = int(input())
arr = list(map(int, input().split()))
arr.sort()

l = len(arr)
q1 = None
q2 = None
q3 = None

#can be compacted as q1 & q2 are same. But just for more clarity
if l % 2 == 0:
  q1 = median(arr[0:(l//2)])
  q2 = median(arr)
  q3 = median(arr[(l//2):])
else:
   q1 = median(arr[0:(l//2)])
   q2 = median(arr)
   q3 = median(arr[((l//2) + 1):])

print(q1)
print(q2)
print(q3)
