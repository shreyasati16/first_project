# def fact_recursive(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n* fact_recursive(n-1)
# print(fact_recursive(5))
def is_leap(year):
    leap = False
    leap2 = True
    if(year/4==0):
        return leap2
    else:
        return leap

year = int(input(2012))
print(is_leap(year))