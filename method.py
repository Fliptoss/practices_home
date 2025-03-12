def main():
    x = int(input("What is x?"))
    print("x is the square of ",square(x))

def square(n):
    #return n ** 2
    return pow(n,2)

main()