# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

numbers = list(map(int, input().split()))
weights = list(map(int, input().split()))

product = [num*weight for num, weight in zip(numbers, weights)]
weighted_mean = round(sum(product) / sum(weights), 1)

print(weighted_mean)
