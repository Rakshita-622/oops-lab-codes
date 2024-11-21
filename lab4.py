#LAB 04
#Pattern Printing, Strings

"""1"""
"""1 2"""
"""1 2 3""" 
"""1 2 3 4""" 
"""1 2 3 4 5"""

for i in range (1,6):
    for j in range (1,i+1):
        print(j,end=" ")
    print("")


"""1"""
"""2 2"""
"""3 3 3""" 
"""4 4 4 4""" 
"""5 5 5 5 5"""

for i in range (1,6):
    for j in range (1,i+1):
        print(i,end=" ")
    print("")


"""A"""
"""B B"""
"""C C C""" 
"""D D D D""" 
"""E E E E E"""

for i in range (1,6):
    for j in range (1,i+1):
        print(chr(i+64),end=" ")
    print("")


"""*****""" 
"""****""" 
"""***""" 
"""**"""
"""* """

for i in range (1,6): 
    for j in range (i,6):
        print("*",end=" ")
    print("")


"""1 2 3 4 5"""
"""1 2 3 4""" 
"""1 2 3""" 
"""1 2"""
"""1 """
for i in range (1,6): 
    k=1;
    for j in range (i,6): 
        print(k,end=" ")
        k+=1
    print("")


""" 1 
   121
  12321
 1234321
123454321"""

n=int(input("Enter n : "))
for i in range (1,n+1): 
    k=1
for j in range (i,n): 
    print(" ",end="")
    for j in range (1,i+1): 
        print(k,end="") 
        k+=1
        x=k-1
    for j in range (1,i):
        x-=1
        print(x,end="")
print("")


# String
# 1.	Write a program to separate the following string into comma (,) separated values. 
# X= “ India.is.my.country”
# 2.	Write a program to sort strings alphabetically in python.
# 3.	Write a program to remove a given character from a string.
# Y=”M.A.N.I.P.A.L”
# 4.	Write a program to remove the (.) dots from the above string.
# 5.	Write a program to take an input from a user as a string then, reverse it.
# 7.	Write a program to check if a string contains only digits.
# 8.	Write a program to check if a string is palindrome or not?
# 9.	Write a program to find the number of vowels in the string.
# 10.	Write a program to check if every word in a string begins with a capital letters or not.

#Q1
x= "India.is.my.country"
z=x.replace(".",",")
print(z)

#Q2
y="manipal"
X=list(y)
X.sort()
y=str(X)
print(y)

#Q3
a="manipal"
b=list(a)
b.remove("a")
for i in b:
    print(str(i),end="")

#Q4
print("")
Y="M.A.N.I.P.A.L"
print(Y.replace(".",""))

#Q5
for i in range (len(Y)-1,-1,-1):
    print(Y[i],end="")

#Q7
print("")
if Y.isdigit():
    print("Yes")
else:
    print("NO")

#Q8.
Y="ABA"
Y1=Y[::-1]
if (Y==Y1):
    print("Yes")
else:
    print("NO")

#Q9. 
vowels=['a','e','i','o','u']
c=0
sentence="hello how are you"
for word in sentence:
    for alphabet in word:
        if alphabet in vowels:
            c +=1
print(c)

#Q10. 
sentence="hello how are you"
if (sentence[0][0][0]).isupper():
    print("Yes")
else:
    print("NO")
