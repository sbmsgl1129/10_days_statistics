# Enter your code here. Read input from STDIN. Print output to STDOU
from operator import itemgetter
from collections import defaultdict

n = int(input())
array = list(map(int, input().split()))
sorted_array = sorted(array)

#Calculating mean
mean = round((sum(array) / n), 1)

#Calculating median
median = None
length = len(sorted_array)
if length % 2 == 0:
  median = round((sorted_array[(length // 2) - 1] + sorted_array[(length // 2)]) / 2, 1)
else:
  median =  sorted_array[length // 2]


#Calculating mode
num_count = defaultdict(lambda: 0)
for num in sorted_array:
    num_count[num] += 1
mode = max(num_count.items(), key=itemgetter(1))[0]

print(mean)
print(median)
print(mode)
