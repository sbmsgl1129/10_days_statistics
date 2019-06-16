# Enter your code here. Read input from STDIN. Print output to STDOUT
x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]

n  = 5

sum_x = sum(x)
avg_x = sum_x / n

sum_y = sum(y)
avg_y = sum_y / n

square_sum_x = sum([i*i for i in x])
sum_xy  = sum([i*j for i,j in zip(x,y)])

coeff = ((n*sum_xy) - (sum_x*sum_y)) / ((n*square_sum_x) - (sum_x*sum_x))
intercept  = avg_y - (coeff*avg_x)

print("{:.3f}".format(coeff*80 + intercept))

