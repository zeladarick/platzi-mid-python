# is num divisible by x <-> is num multiple of x
def is_x_divisible(num, x):
    return (num % x) == 0 

def run():
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
    



if __name__ == '__main__':
    run()