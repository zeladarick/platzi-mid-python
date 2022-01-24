from functools import reduce

def run():
    #A function is called 'high order function' ir satisfied one of this premises
    #   - Recive a function as parameter
    #   - Return a function

    #Common high order functions are:

    #----- filter(conditional_function, iterable) -----    
    #Takes every element of iterable
    #If the conditional function aplied to the element returns True...
    #then, the element is added to the new iterable
    #Returns the new iterable

    #Example
    numbers_list = [1, 4, 5, 6, 9, 13, 19, 21]
    odd_numbers_list = list( 
        filter( lambda x : (x % 2) != 0 , numbers_list ) 
    )    
    print(odd_numbers_list)
    
    #----- map(changer_function, iterable) ----- 
    #Takes every element of iterable
    #Then, add to the new iterable the result of...
    #apply changer function to the iterable element
    #Returns the new iterable

    #Example
    numbers_list = [1, 2, 3, 4, 5]
    square_numbers_list = list( 
        map( lambda x : x **2 , numbers_list) 
    )
    print(square_numbers_list)

    #----- reduce(operating_function, iterable) ----- 
    #Operating function must have two parameters
    #At fist iteration, takes two elements of the iterable
    #Then, apply the operating function to this two elements
    #Saves previous result of applying the operating function
    #Next, apply the function to...
    #the previous saved result and next iterable element
    #Repeat that until the iterable ends (changing saved value)
    #Returns the saved value

    #Example
    numbers_list = [2, 2, 2, 2, 2]
    all_multiplied = reduce( lambda x,y: x*y, numbers_list)
    print(all_multiplied)


if __name__ == '__main__':
    run()