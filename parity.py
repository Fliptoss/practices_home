def main():
    x = int(input("Enter the number x?\n"))
    if even(x):
        print("Even")
    else:
        print("Odd")



def even(n):
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False
    return True if n % 2 == 0 else False


main()