import sys

# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("too few arguments")

if len(sys.argv) < 2:
    print("too many arguments")
elif len(sys.argv) > 2:
    print("too many arguments")
else:
    print("my name is", sys.argv[1])  

