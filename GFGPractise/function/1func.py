def fun2():
    print("Inside fun2()")
def fun1():
    print("Before fun2()")
    fun2()
    print("after fun2()")
print("Before fun2()")
fun2()
print("After fun()")