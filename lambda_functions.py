def run():
    #Lambda function example
    lambda_sum = lambda x,y : x + y

    #Normal function example
    def sum(x,y):
        return x + y

    #Types printing
    print("Lambda function type: ", type(lambda_sum))
    print("Normal function type: ", type(sum))

    #Results printing
    print("Lambda function result: ", lambda_sum(2,6))
    print("Normal function result: ", sum(2,6))
    
    #Lambda and normal functions are almost the same
    #(they are even the same variable type)
    #But Lambda functions are usefull to improve code legibility

if __name__ == '__main__':
    run()