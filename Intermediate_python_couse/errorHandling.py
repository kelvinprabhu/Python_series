# Error Handling in Python
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print(f"Result: {result}")
finally:
    print("Execution completed.")
# Custom Exception
