# 7. Write a python program to access a function inside a function.

# defining a function
def fun1(x, y):
    # defining a function inside function
    def fun2():
        print(x + y)

    # calling the inner function
    fun2()


# calling the outer function
fun1(45, 76)
