# local variable --  variable defined inside the function
def my_function():
    local_var = 10  # local variable
    print("Local variable:", local_var)
my_function()
# print(local_var)  # This will raise an error because local_var is not defined outside
# global variable -- variable defined outside the function
global_var = 20  # global variable
def my_function2():
    print("Global variable:", global_var)
my_function2()