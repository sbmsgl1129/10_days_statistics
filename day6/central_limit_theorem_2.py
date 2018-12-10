# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def norm_cdf(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean)/math.sqrt(2 * std**2)))

mean = 240
std = 20
print(round(norm_cdf(250,mean,std),4))
