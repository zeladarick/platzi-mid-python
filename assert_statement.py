#The assert statements are a fancy way to raise an Exception in Python
#   assert condition, error_message
#If the condition is FALSE, then throws an Exception with error_message message

def run():
    num_str = input("Enter a number: ")
    try:
        num = int(num_str)
        #assert statement
        assert num >= 0, "Negatives not allowed" 
        num_factorial = factorial(num)        
        print("Factorial of " + num_str + " is: ", num_factorial)
    except Exception as e:
        print("Invalid input: ", e)

#Calculates and return num! (num factorial)
def factorial(num):
    if(num == 0):
        return 1
    else:
        return factorial(num - 1) * num
    
if __name__ == '__main__':
    run()