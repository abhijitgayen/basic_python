myList=["it","is","see","now","by","abhijit", "gayen","ram","shyam",12] # in my list i will be able to store  string,integer, floating point,
print(myList)
print(myList[5])# using index we able to find the exactly the string
myNumber=[12,15,14,1,2,3,-50,158,123,12]#a list contains more than one data type
print("my list is ",myNumber)
print("max in list ",max(myNumber),"\nmin of this list is ", min(myNumber))#we able to apply min() ,max() function if 
#the list contains same data type.it is working for number s
myNumber.sort()#it is ran on same data types and also ran for each cases
print("my list after sorting",myNumber)
myNumber.reverse ()
print("After reversing this myList is :",myNumber)
print(myNumber[1:6])
print(myNumber[ : : -1])# we see allthing in the string
myNumber.append( 123)# add this number in the end of this list
print(myNumber)
#there are another way to concate two list directly
Numberlis=['tygh',5,6,78,390]
myNumber.extend(Numberlis)
print('After extend the new list is',myNumber)
myNumber.insert( 0,156)# insert the elemt at the position of index 0
print(" Insert element in this list we get",myNumber)
myNumber.remove(1)#myNumber.remove(name_data_for_delete)
print("after removing the element  1 in list ", myNumber)
#remove the last element of this list
#it also return the pop elements
Print('pop element is', myNumber.pop())
# Mutable --can change
# Immutable --Cannot change

#all things in list and tuple are same.all property are same
#in tuple you are not able to change data in list directly .
#there are two function i.e tp.count() and tp.index()
tp=(1,45,12)
print(tp)
# tp[0]=12 not ran rhis portion because this is a immutable
#how to swap two elelment in the python
a=123
b=45
a,b=b,a
# temp=a
# a=b
# b=temp
print(a,b)
