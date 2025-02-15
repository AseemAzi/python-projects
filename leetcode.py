# Find Greatest Common Divisor of Array

num = [2,5,6,9,10]
s = num[0]
l = num[0]
m = 0
for i in num:
    if i < s:
        s=i
    elif i > l:
        l=i
for i in range(1,l+1):
    if s%i==0 and l%i==0:
        m = i
        if i > m:
            pass
        
print("smallest number is:",s)
print("largest number is:",l)
print("common divisor is:",m)
        

# Number of Employees Who Met the Target

hours = [9,7,3,5,4,6]
tot = 0
for i in hours:
    if i > 5:
        tot+=1
print("total number of employees met target:",tot)

