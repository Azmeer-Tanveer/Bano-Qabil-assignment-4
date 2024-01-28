#Python Program to count unique values inside a list

a_list = [1,5,7,9,8,5,6,5,4,7,1,1,5,7,8,9,]
print(a_list)
unique_list = list(set(a_list))
a=len(unique_list)
print("Number of unique values:", a)


#program to generate dictionary

print("program to generate a dictionary ")


def dic(a):
    n={}

    for i in range(1, a+1):
        n[i]=i*i

    return n

a=int(input("Enter value of n :"))
square=dic(a)

print("Genrated Dictionary:  ")
print(square)

#Sum of numbers


number = []

n = int(input("Enter the number of numbers you want to input: "))

for i in range(n):
    num = float(input(f"Enter number {i + 1}: "))
    
    number.append(num)

total = sum(number)
print("Numbers entered:", number)
print("The sum of numbers is",total)


#Fibionacci series


def fbseries(n):
    fib=[0,1]


    while len(fib) < n:
        numb=fib[-1]+fib[-2]
        fib.append(numb)
    return fib

value = int(input("Enter the number of terms in the Fibonacci series: "))
result=fbseries(value)

print("Fibonacci series with",value , "terms:")
print(result)











