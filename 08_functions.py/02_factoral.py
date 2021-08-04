def fact_iter(n): #this is function
    product=1
    for i in range(n):
        product=product*(i+1)
    return (product)
print(fact_iter(7)) #calling the function fact_iter