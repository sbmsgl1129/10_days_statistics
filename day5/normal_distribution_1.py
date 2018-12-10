# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def norm_cdf(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean)/math.sqrt(2 * std**2)))


print(round(norm_cdf(19.5, 20, 2), 3))
print(round(norm_cdf(22, 20, 2) - norm_cdf(20, 20, 2), 3))
