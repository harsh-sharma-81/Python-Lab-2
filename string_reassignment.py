def change_string(s):
    list2=list(s)
    print(s)
    s[0]="X"
    l="".join(s)
    print("Updated string:",l)

#We'll make this string as a list with every character as individual element and then replace the first index with 'X'
list2=list(input("Enter a string:"))
str2="".join(list2)
print(str2)
change_string(list2)