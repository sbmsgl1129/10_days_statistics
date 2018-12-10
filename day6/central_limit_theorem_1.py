# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def norm_cdf(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean)/math.sqrt(2 * std**2)))

mean = 205*49
std = 15*7
print(round(norm_cdf(9800, mean, std), 4))
