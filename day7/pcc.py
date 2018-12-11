# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def mean(x):
  return sum(x)/len(x)

def standard_deviation(x):
  arr_mean = mean(x)
  square_distance_from_mean = [(num - arr_mean)**2 for num in x]
  avg_square_distance_mean  = mean(square_distance_from_mean)
  return math.sqrt(avg_square_distance_mean)

def covariance(x,y):
  mean_x = mean(x)
  mean_y = mean(y)

  distance_from_mean_x = [i-mean_x for i in x]
  distance_from_mean_y = [i-mean_y for i in y]
  product_of_distances = [i*j for i,j in zip(distance_from_mean_x,distance_from_mean_y)]

  return sum(product_of_distances)/len(product_of_distances)

n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

print(round(covariance(x,y) / (standard_deviation(x)*standard_deviation(y)), 3))
