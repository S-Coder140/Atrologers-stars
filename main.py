# astrologers stars
print("give the no. of rows")
rows = int(input())
print("write true(1) or false(2) ")
x = int(input())
if x == 1:
    for i in range (1,rows+1):
        print(i*"*")
elif x == 2:
    for i in range (1, rows + 1):
        i1 = rows+1 - i
        print(i1*"*")
