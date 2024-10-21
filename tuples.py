#creation
#access
#unpacking
#nested
#count
#index
#change into list and back to tuple

my_tuple = (1,2,3,3,4,5,3,6)
print(type(my_tuple))

tup_lis = list(my_tuple)    #change tuples to list
print(type(tup_lis))

change = tup_lis.pop(3)
print(type(change))

lis_tup = tuple(tup_lis)  #change list to tuple
print(type(lis_tup))

print(lis_tup)

print(my_tuple)
