#division are different in python. such as
print(5/2)
#however you can round them up again. you get an integer value
print(5//2)

#careful with rounding up negative number as it will round up to the highest vaule but it is not the answer
print(-3//2)
#the answer is -2 but the answer should be somewhere -1.5. 
#so to solve this we will find the decimal first and then integer that number
print(int(-3/2))
#you will get the integer value of that number 

print("--------------------------------------")

#modding is similar to most languages 
#n = 10/3
#print(f"{n:.2f}")
print(f"{10/3:.2f}")

#again for negative value the number will be 
print(-10%3) #output is 2. but we want the output to be 1

print("--------------------------------------")

#so for that reason we introduce math
import math
print(math.fmod(-10,3))  #output is -1.0  which is the correct output 

print(math.floor(3/2))
print(math.ceil(3/2))
print(f"{math.sqrt(2):.2f}")
print(math.pow(2,3))

print("--------------------------------------")

#min and max infinity values
# flaot("inf")
# float("-inf")


print(math.pow(2,200) < float("inf")) #the output will be true as python numbers are infinite

print("--------------------------------------")

#arrays are called list in python and they are dynamic therefore they can be used as stack
arr = [1,2,3]
print(arr)

#appending and poping 
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

#you can also insert value but it gives a big O(n) notation
arr.insert(0,8)
print(arr)
#you can also get a sublist of an array
arr2 = [1,2,3,4,5,6]
print(arr[1:3])  #will print out the 2nd and 3rd index but not the fourth index

print("--------------------------------------")

#unpacking 
a,b,c = [1,2,3] #keep in mind that the variable on the left side should have the same number of values on the 
#right side

print("--------------------------------------")

for i in range(len(arr)):
    print(i)

#without using index
for n in arr:
    print(n)

#if you want the index number as well as the values then 
#we can use "enumerate"

for i, n in enumerate(arr):
    print(i, n)

print("--------------------------------------")

#if we want to go through multiple arrays we can use "zip"
num1 = [1,3,5]
num2 = [2,4,6]

for n1, n2 in zip(num1, num2):
    print(n1, n2)

print("--------------------------------------")

#reverse the array
n = [1,2,3,4]
n.reverse()
print(n) 