# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

#https://stackoverflow.com/a/9448324
def norm_cdf(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean)/math.sqrt(2 * std**2)))

print(round((1-norm_cdf(80, 70, 10))*100, 2))

print(round((1-norm_cdf(60,70,10))*100, 2))

print(round(norm_cdf(60,70,10)*100, 2))
