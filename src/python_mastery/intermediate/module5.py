# Exception handling
# Exception handling is very important to make sure to attend possible edge cases and make sure to not to break the system

# try block is used to write risky code
# except block is to handle the exception
# else block is to do something only when no exception raise
# finly bock us used as cleanup, get executed always

if __name__ == "__main__":
    name = "abc"
    try:
        x = name % name
    except ValueError, TypeError:
        print("Something went wrong")
    else:
        print("All went well")
    finally:
        print("Printing alwyas")
