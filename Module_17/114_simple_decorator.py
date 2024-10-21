user = {"username": "jose123", "access_level": "admin"}

def user_has_permisions(func):
    def secure_func():
        if user.get("access_level") == "admin":
            return func()

    return secure_func

def my_function():
    return "Password for admin panel is 1234."

my_secure_function = user_has_permisions(my_function)

print(my_secure_function())
        
