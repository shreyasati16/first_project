def num_recurse(n):
    if n==1 or n==0:
        return 1
    else:
        return n*(n+1)/2

print(num_recurse(10))