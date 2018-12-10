# Enter your code here. Read input from STDIN. Print output to STDOUT
def fact(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

e = 2.71828
print(round((2.5**5)/((e**2.5)*fact(5)), 3))
