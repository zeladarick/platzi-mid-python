#File Management in Python
#Use with open(path, opening_type, encoding="utf-8") as f
#"With" clausule creates a safe background for file working

#Read from a file
def read():
    numbers = []
    with open("./file_resources/numbers.txt", "r", encoding="utf-8") as f:
        for row in f:
            numbers.append(int(row))

    print(numbers)

#Write in a file
def write():
    names = ["Facundo", "Miguel", "Pepe"]
    writing_mode = "w" #w=write,a=append
    with open("./file_resources/names.txt", writing_mode ,encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    write()

if __name__ == '__main__':
    run()