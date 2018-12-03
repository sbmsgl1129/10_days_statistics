# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def mean(list):
    return round(sum(list)/len(list), 1)

n = int(input())
arr = list(map(int, input().split()))

arr_mean = mean(arr)
square_distance_from_mean = [round((float(num) - arr_mean)**2 , 1) for num in arr]
avg_square_distance_mean  = mean(square_distance_from_mean)
std_deviation = round(math.sqrt(avg_square_distance_mean), 1)

print(std_deviation)
