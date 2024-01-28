# try block
try:
    a = int(input("Enter numerator number: "))
    b = int(input("Enter denominator number: "))
    c = a/b
    print("Result of Division:" , c)
    # to manually raise an exception
    raise ValueError("Incorrect Value")

# except block handling division by zero
except(ZeroDivisionError):
    print("You have divided a number by zero, which is not allowed.")

# except block handling wrong value type
except(ValueError):
    print("You must enter integer value")

except:
    print("Oops! Something went wrong!")

# finally will be executed even if the exception is not handeled    
finally:
    print("Code execution Wrap up!")
