def remove_last(list1):
    list1.pop()
    print("List after:",list1)

list1=list(map(int,input("Enter integers into list:").split()))
print("List before:",list1)
remove_last(list1)