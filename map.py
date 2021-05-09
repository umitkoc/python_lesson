#                   map function 

#iterable as list or array
#function as def or lambda
#map(function,iterable) or

numbers=[1,2,3,4,5,6]
#example 
def Sqrt(number):
    return number**2
a=list(map(Sqrt,numbers))
print(a)

#example
b=list(map(lambda number:number**3,numbers))
print(b)

#map(str,int,double variable as convert,iterable)
#example
str_numbers=["1","2","3","4","5","6"]
c=list(map(int,str_numbers))
print(c)
