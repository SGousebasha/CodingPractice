"""print(len("Hurry Potter\n"))
"""
"""class Solution:
    def numberOfSteps(self,num: int)->int:
        #result = 0
        while(num>0):
            if (num%2!=0):
                num-=1
            if (num%2==0):
                num = int(num/2)
            if (num%2!=0):
                num - 1


"""
"""def fib(x):
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)
print(fib(4))
"""

"""from cgi import print_directory
import math
from traceback import print_tb

#n = int(input())
list1 =[1,2,35,3,6,2]
print(list1) #list(map(int,input().split()))
list2 = [3,8,9,4,6]#list(map(int,input().split()))
print(list2)
list1.extend(list2)
list1.sort()
print(list1[])"""


"""a = int(input("Enter a value"))
b = int(input("Enter b value"))
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
"""

"""def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 400 == 0):
        return True
    if (year % 100 == 0):
        return leap
    if (year % 4 == 0):
        return True
    else:
        return False  
    
    return leap
year = int(input())
print(is_leap(year))"""
"""def chackLeap(year):
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 ==0) and (year % 100 != 0):
        return True

    else:
        return False
print(chackLeap(int(input())))"""




"""n = int(input())
a = []
for i in range(n):
    c = int(input())
    a.append(c)

print("before sorting",a)
a.sort()
print("after sortng",a)
print("The second maxNumber:",a[-2])"""
"""from cgi import print_environ
from itertools import permutations, product
letters = (1,1,1)
a = list(product(letters,range(len(letters))))
print(a)"""
"""(0,0,0)
(0,0,1)
(0,1,0)
(1,0,0)"""
#(1,2)
"""(1,1)
(1,2)
(2,1)
(2,2)"""
"""n = int(input())
a = []
newList = []
for i in range(n):
    c = input()
    a.append(c)

print(a)
chack = 0
for j in range(len(a)):
    print("the j value is ",j)
    for k in range(1,len(a)-j):
        print("the K value is ",k)
        if(a[j]==a[k]):
            chack += 1
    if (chack==0):
        
        newList.append(a[i])
print(newList)"""
        

# Python program to print
# duplicates from a list
# of integers
"""def Repeat(x):
	_size = len(x)
	repeated = []
	for i in range(_size):
		k = i + 1
		for j in range(k, _size):
			if x[i] == x[j] and x[i] not in repeated:
				repeated.append(x[i])
	return repeated"""

# Driver Code
"""list1 = [10, 20, 30, 20, 20, 30, 40,
		50, -20, 60, 60, -20, -20]
print (Repeat(list1))"""
	
# This code is contributed
# by Sandeep_anand


#Finding Douplicates

"""numEle = int(input())
ele = []
for a in range(numEle):
    c = int(input())
    ele.append(c)
newList = []
for i in range(len(ele)):
    for j in range(i+1,len(ele)):
        if (ele[i]==ele[j]) and (ele[i] not in newList):
            newList.append(ele[i])
print(newList)"""


# Two varibles swaping
"""a = input()
b = input()
a,b = b,a
print(a)
print(b)"""


# Finding even elements in a given list


"""list1 = list(map(int,input().split()))
list2 = []
list3 = []
for i in list1:
    if (i%10==0):
        list2.append(i)
if (len(list2)==len(list1)):
    for j in list1:
        if (j%20==0):
            list3.append(j)
    print(list3)
else:
    for a in list1:
        if (a%2==0):
            list2.append(a)
    print(list2)"""

# pyrmid

"""a = 1 
for i in range(1,5+1):
    for j in range(i):
        print(a,end=" ")
        a+=1
    print()"""


#from readline import append_history_file
"""l = []
n = int (input())
new = []
for i in range(n):
    c = int(input())
    l.append(c)

for a in l:
    n =l.count(a)
    if (n>1) and a not in new:
        new.append(a)
print(new)
"""


"""n = input("Enter a string")
res = ''
for i in range(len(n)):
    if (i<len(n)-1):
        res = res + n[i]+"@"
    else:
        res+=n[i]
print(res)"""


"""n = int(input("Enter a number"))
m = n
if (m<0):
    n=n*-1
res = 0
while n>0:
    last = n%10
    res = res*10 + last
    n=n//10

if (m<0):
    print(res*-1) 
else:
    print(res)
"""

"""print(ord("@"))"""
"""char_frequency(str1):
    dictinary = {}
    for n in str1:
        keys = dictinary.keys()
        if n in keys:
            dictinary[n] += 1
        else:
            dictinary[n] = 1
    return dictinary
print(char_frequency('google.com'))"""

"""from itertools import product
a = {1,2}
print(list(product(range(4),a)))"""
"""from tkinter import N"""


"""from tkinter import N


nums = {1,2,3,4,5,6}
nums = {0,1,2,3} & nums
nums = filter(lambda x: x>1,nums)
print(list(nums))"""

"""def power(x,y):
    if (y==0):
        return 1
    else:
        return x * power(x,y-1)
print(power(2,3))"""


# Question from Amazon ; Finding max profit

"""n = list(map(int,input().split()))
byPrice = n[0]
maxProfit = 0
for i in n:
    if (byPrice>i):
        byPrice=i
    a = i-byPrice
    if (a>maxProfit):
        maxProfit=a
print(maxProfit)"""

    
# Question from Google | Findign disapear Number

"""result = []
for i in range(min(list1),max(list1)):
    if i not in list1:
        result.append(i)
result = sorted(result + list1)
print(result)"""

# finding pivot element
"""nums=[-1,-1,0,0,-1,-1]
lsum = 0
rsum = sum(nums)
a = 0
b = 0
for i in range(len(nums)):
    rsum -= nums[i]
    if (lsum==rsum):
        b+=1
        a = i
        break
    lsum+=nums[i]

if (b!=0):
    print(a)
else:
    print(-1)"""

# isomorpic String or not 

"""
from itertools import count
from multiprocessing import parent_process
from typing import Counter


s = "paper"
c = 1
for i in range(len(s)):
    a=s[i::]
    if s[i] in a:"""


# finding a max area of water container from Udemy

"""import math


list1 = list(map(int,input().split()))
w = 0
h = 0
result = 0
for i in range(len(list1)):
    for j in range(1,len(list1)):
        w = j-i
        h = min(list1[j],list1[i])
        r = w*h
        if r>result:
            result = r
print(result)"""

# Findin isomarphic str or not

"""s = "foo"
t = "bar"
d = {}
def chackiso(s,t):
    for i in range(len(s)):
        c1,c2 = s[i],t[i]
        if c1 not in d:
            if c2 in d.values():
                return False
            d[c1] = c2
        elif d[c1] !=c2:
            return False
    return True
print(chackiso("egg","add"))
"""

# Find the max sum  of a subsequence with constrain that no adjust element added to it

"""from cgi import print_environ


arr = [5,5,10,100,10,5]
s = 0
s1 = 0
for i in range(0,len(arr),2):
    s+=arr[i]
for i in range(1,len(arr),2):
    s1+=arr[i]

print(max(s,s1))
"""

# Reversing a string

"""str1 = "Hello"

def chackRev(str1):
    str2 = ''
    i=len(str1)-1
    while i>=0:
        str2+=str1[i]
        i-=1
    return str2
print(chackRev(str1))"""

# merge&sort

"""a = [0,3,4,31,1,14,54,2]
b = [4,6,30]
for i in b:
    a.append(i)
print("Unosrted are Array: ",a)
for i in range(len(a)-1):
    if (a[i]>a[i+1]):
        a[i],a[i+1]=a[i+1],a[i]
print("sorted array ", a)"""
"""def chack(nums):    
    nums = sorted(nums)
    a = 0
    b = len(nums)-1
    res = []
    while b-a==1:
        if (nums[a]+nums[b]==target):
            res.append(a)
            res.append(b)
            return res
        elif (nums[a]+nums[b]>target):
            b-=1
        elif (nums[a]+nums[b]<target):
            a+=1
chack([])"""

# Chacking for reaccurance of Element

"""a = [2,5,1,2,3,5,1,2,4]
dicttion = {}
for i in range(len(a)):
    if a[i] not in dicttion:
        dicttion[a[i]]=1
    else:
        x=dicttion[a[i]]
        dicttion[a[i]]=x+1
print(dicttion)"""


"""def even_numbers(n): 
    if n <= 0: 
        return [] 
    else: 
        return [n] + even_numbers(n-2)
  
n = int(input('enter a number : '))  
print(even_numbers(n))"""

"""a = int(input("enter a amount"))
b = float(input("enter percentage of interst"))
moths = int(input("for how many moths ?"))

result = moths*((a*b)/100)

print(result)"""

# n = int(input("Enter a 4Digit number"))
# a = []
# while n>0:
#     r = n%10
#     a.append(r)
#     n//=10
# a=sorted(a)
# a[1],a[2] = a[2],a[1]
# a1 = str(a[0])+str(a[1])
# a2 = str(a[2])+str(a[3])
# print(int(a1)+int(a2))

# a ="apple"

# def do_allocation(number_of_people, number_of_buses):
#   # Initialize the list of bus capacities with the capacity of the first bus
#   bus_capacities = [1]
  
#   # Calculate the capacity of each bus
#   for i in range(1,number_of_buses - 1):
#     bus_capacities.append(bus_capacities[i - 1] + bus_capacities[i])
  
#   # Initialize the list of people on each bus with 0
#   people_on_buses = [0] * number_of_buses
  
#   # Iterate over the buses and allocate people to each bus
#   for i in (0,number_of_buses - 1):
#     if number_of_people > 0:
#       # Allocate as many people as the bus can hold
#       people_on_buses[i] = min(number_of_people, bus_capacities[i])
      
#       # Decrement the number of people remaining to be allocated
#       number_of_people = number_of_people - people_on_buses[i]
  
#   # Return the list of people on each bus
# print(do_allocation(10,5))


"""def do_allogate(a,b):
    bc = [1]
    i = 1
    flag= False
    while (i<=b):
        chack = 0
        if (i==1):
            bc.append(1)
        elif(i>1):
            chack1 = sum(bc)
            tcal = bc[i-1]+bc[i-2]
            chack = chack1+tcal
            if (chack<=a):
                bc.append(tcal)
            elif (chack>a and flag==False):
                last_bus_cap = a-chack1
                bc.append(last_bus_cap)
                flag=True
            else:
                bc.append(0)
        i+=1
    return bc
print(do_allogate(10,5))"""

"""def isPalindrome(s):
    st = ""
    for i in range(len(s)):
        if (s[i].isalnum()):
            st+=lower(s[i])
    n = len(st)-1
    def polindromHelper(st,start,end):
        if (start>=end):
            return True
        elif(st[start]!=st[end]):
            return False
        polindromHelper(st,start+1,)"""

# x = "ABC"
# x = x.lower()
# print(x)
        
# def numberPyramid(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(str(j)+" ",end="")
#         print()
# print(numberPyramid(5))

"""def numberOfPairs(arr):
    result =  0
    sockPair = {}
    for i in arr:
        if (i in sockPair):
            sockPair[i]+=1
        else:
            sockPair[i]=1
    for i in sockPair:
        a = sockPair[i]//2
        result+=a
    return result
print(numberOfPairs([1,2,1,3,2]))"""

"""d1 = {"name":"gouse","class":"B.tech"}
for i in d1:
    print(d1[i])"""
"""def compareTriplets(a, b):
    # Write your code here
    p1 = 0
    p2 = 0
    for i in range(len(a)):
        if (a[i]>b[i]):
            p1+=1
        elif (a[i]<b[i]):
            p2+=1
    print([p1,p2])
print(compareTriplets([5,6,7],[3,6,10]))"""

# def beauty(n,m,s,x,y):
#   edges={}
#   for i in range(m):
#     if edges.get(x[i]):
#       edges[x[i]]+=[y[i]]
#     else: edges[x[i]]=[y[i]]

  
#   def maxi(lis):
#     if lis==[]: return 0
#     k={}
#     ma=0
#     for i in lis:
#       kk=s[i-1]
#       if k.get(kk) is None:
#         k[kk]=1
#       else: k[kk]+=1
#       if k[kk]>ma: ma=k[kk]
#     return ma
  
  
#   def path(node,done):
#     if node in done: raise Exception
#     if edges.get(node) is None: return [done+[node]]
#     temp=[]
#     for i in edges[node]:
#       temp+=path(i,done+[node])
#     return temp
  
#   ma=0
#   try:
#     for i in range(1,n+1):
#       for j in path(i,[]):
#         mm=maxi(j)
#         if mm>ma: ma=mm
#     return ma
#   except Exception:
#     return -1

# n=int(input())
# m=int(input())
# s=input()
# x=list(map(int,input().split()))
# y=list(map(int,input().split()))


# Creating a matrix

# m = [[1,2,3],[4,5,6],[7,8,9]]
# rows = len(m)
# columns = len(m[0])
# print(columns)
# s = 0
# e = rows*columns-1
# mid = (s+e)//2
# print("the mid val",mid)

# print(m[mid//columns][mid%columns])

# class Vehicle():
#     def __init__(self,initial_fuel,mileage,fuel_left):
#         self.mileage = mileage
#         self.fuel_left = fuel_left
#         self.initial_fuel = initial_fuel

#     def identify_disctance_that_can_be_travelled(self):
#         cf = 0
#         cf = self.fuel_left-5
#         if (self.fuel_left>5):

#             return self.mileage*cf
#         else:
#             return 0
#     def identify_distance_travelled(self):
#         dis = 0
#         cf = 0
#         cf = self.fuel_left-5
#         dis = self.initial_fuel-cf
#         return dis*self.mileage
# obj = Vehicle()
# print(obj.identify_disctance_that_can_be_travelled())
# print(obj.identify_distance_travelled())
# print(21%17)


# this is a program to print even or odd

a = int(input("Enter a number"))
if (a%2==0):
    print("even number")
else:
    print("odd")
