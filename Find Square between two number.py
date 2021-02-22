
def squares(a, b):
    lists=[]
    for i in range (a,b+1):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists
x = int(input("Enter the Number 01: "))
y = int(input("Enter the Number 02: "))
print(squares(x, y))
