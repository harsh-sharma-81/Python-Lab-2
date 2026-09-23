def add_entry(d):
    print("Enter new key-value pair")
    key=input("Input key:")
    value=input("Input value:")
    d[key]=value
    print("New dictionary:",d)

#Here we'll make a dictionary and use loop to enter elements
d1={}
n=int(input("Enter number of elements to be put in dictionary:"))

for i in range (n):
    key=input("Enter key: ")
    value=input("Enter value: ")
    d1[key]=value

print("Dictionary before:", d1)
add_entry(d1)