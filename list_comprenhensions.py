def run():
    #----- Lists Comprenhensions ----- 
    #Usefull to create a new list with the items of other list 
    #Basic structure
    #   new_list = [new_list_item(i) for i in iterable if condition(i)]
    #Notice that new_list_tem and condition are functions of i
    #new_list_item item is added only if actual i satisfied condition (returns True)
    challenge()

# is num divisible by x <-> is num multiple of x
def is_x_divisible(num, x):
    return (num % x) == 0 

def challenge():
    result = [ i for i in range(1, 100000)
    if (
        is_x_divisible(i, 4) and
        is_x_divisible(i, 6) and
        is_x_divisible(i,9)
    )]

    print(result)

def printSquares():
    squares = []
    
    #With loops
    for i in range(1, 101):
        if not is_x_divisible(i, 3):
            squares.append(i**2)
    
    #With list comprenhensions
    squares = [ i**2 for i in range(1, 101) if not is_x_divisible(i, 3)]

    print(squares)   

if __name__ == '__main__':
    run()