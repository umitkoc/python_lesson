#                   map function 

#iterable as list or array
#function as def or lambda
#map(function,iterable) or

numbers=[1,2,3,4,5,6]
#example 
def Sqrt(number):
    return number**2
list(map(Sqrt,numbers))

#example
list(map(lambda number:number**3,numbers))

#map(str,int,double variable as convert,iterable)
#example
str_numbers=["1","2","3","4","5","6"]
list(str_numbers)
list(map(int,str_numbers))