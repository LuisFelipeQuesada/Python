def greet(func):
    def say_hello():
        print("Hello")
        func_var = func(*args)
        return say_hello
        return func_var

# define another function called say_hello() which prints something and by calling say_hello() at the end, also the greet(func) should be provoked.

def say_hello():
    print("Hello")
print(say_hello())

# write a function called authorize(func)
# define a wrapper (func inside another func) inside and return "Unathorized access" if not authorized.
# define another function to check whether authorized or not. (True or False)
# define the last function named secret_data() to say "This is confidential data" if user is authorized. By calling secret_data you should see if the data is confidential or you will provoke the other function that says "Unauthorized access".
def authorize(func):
    def wrapper():
        if check_authorization():
            return func()
        else:
            return err_msg()
    return wrapper

def check_authorization():
    return True

def secret_data():
    return  "This is confidential data"

def err_msg():
    return "Unauthorized access"

print(authorize(secret_data()))

# write a function called validate(func), define a wrapper inside, see if arguments were not integer, return and error.
# define a function called add(a, b).
# when calling the func add() in the end, if the args are integers return the sum, if even one of them in str, return that error you defined in the first function.
