#    filter
# The filter function is similar to the map function
#example
age=[11,12,15,18,25,26]
def adult(x):             #or lambda x:x>18
    return x>18

list(filter(adult,age))

#example
print(list(filter(lambda x:x>18,age)))

#example
users=[
    {
        "name":"umit",
        "surname":"koc",
        "age":22
    },
    {
        "name":"elif",
        "surname":"ozturk",
        "age":17
    },
    {
        "name":"ali",
        "surname":"koc",
        "age":45

    }

]
list(filter(lambda x:x["age"]>18,users))

