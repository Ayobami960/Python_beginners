# Global variable
name = "John Deo"

def greet():
    # Local variable
    message = "Hello"
    print(f"{message}, {name}!") # Can access both local and global
    print(f"Local variable 'message': {message}")
    
    # call the function
greet()


## Access global variable inside function
print(f"global variable 'name': {name}")