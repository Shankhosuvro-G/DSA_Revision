def prime_number(num):
    count=0
    for i in range (2,num+1):
        if num%i==0:
            count+=1
    if count==1:
        return "Prime Number"
    else:
        return -1
print(prime_number(4))