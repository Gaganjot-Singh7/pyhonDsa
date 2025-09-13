digit=2

def count_digit(digit):
    count=0
    if digit//10==0:
        return count+1
    else:
        n=digit
        while n>0:
            rem=n//10
            n=rem
            count+=1
        return count
print(count_digit(digit))
