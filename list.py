'''
list in python
'''

# students = ["hermionie", "ron", "harry"]

# for student in students:
#     print(student)

def main():
    print_square(4)


# def print_column(column):
#     print("#" * column)

def print_square(size):
    for i in range(size): # 1/2
        for j in range(size): #4
            print("#", end=" ")    
        print()
    # for _ in range(column):
    #     print("?" * column)

main()

'''
#
#
#
'''