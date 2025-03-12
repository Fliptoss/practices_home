# for _ in range(3):
#     print("Meow")

'''
python does not really need to define a variable for a loop. you just simply add "_" instead. 
'''

# while True:
#     n = int(input("what is n?"))
#     if n > 0:
#         break

# for _ in range(n):
#     print("Meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What is n?"))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")


main()