# Enter your code here. Read input from STDIN. Print output to STDOUT

n = 5
p = 1/3
ans = 0.0
for i in range(1,6):
    ans += ((1-p)**(n-i))*p

print(round(ans,3))
