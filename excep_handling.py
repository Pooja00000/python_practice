def divide_numbers():
    try:
        # Get input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Attempt to divide the numbers
        result = num1 / num2
        
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        
    else:
        # If no exception occurs, print the result
        print(f"The result of {num1} divided by {num2} is {result}")
        
    finally:
        print("Execution completed.")

# Run the function
divide_numbers()
