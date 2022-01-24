def run():
    #----- Dictionary Comprenhensions ----- 
    #Usefull to create a new dict with the items of an iterable
    #Basic structure
    #   dict = [dict_key(i) : dict_value(i) for i in iterable if condition(i)]
    #Notice that dict_key, dict_value and condition are functions of i
    #Key/Value item is added only if actual i satisfied condition (returns True)

    challenge()

def challenge():
    cubeNumbers = { i : round(i ** 0.5, 2) for i in range(1, 1001)}
    
    print(cubeNumbers)


def cubeNumbers():
    cube_numbers = {}

    #With loops
    for i in range(1, 101):
        if not is_x_divisible(i, 3):
            cube_numbers[i] = i**3

    #With dict comprenhensions
    cube_numbers = {i : i**3 for i in range(1, 101) if not is_x_divisible(i, 3)}

    print(cube_numbers)
    

# is num divisible by x <-> is num multiple of x
def is_x_divisible(num, x):
    return (num % x) == 0 


if __name__ == '__main__':
    run()