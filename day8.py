#functions 
def saysomething():
    print("hello")
    print("Hows the weather")
    print("How do you do?")

saysomething()

#function with parameters
def greet(name):
    print(f"hello {name}")
    print(f"Hows the weather {name}")
    print("How do you do?")

greet("xyz")

#simple problem with math.ceil function
import math
def print_cal(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"Number of cans will be {num_of_cans}")

test_h = int(input("Height: "))
test_w = int(input("Width: "))
c = int(input("cover: "))
print_cal(height=test_h, width=test_w, cover=c)