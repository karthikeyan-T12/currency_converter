def con(a,b,c):
    while a < 0:
        print("The value you entered",a,"is not \"VALID\"")
        a = float(input("Enter an valid input:"))
    print(a * 85.68) if b == 'inr' and c == 'usd' else print(a * 0.012) if b == 'usd' and c == 'inr' else print( a * 97) if b == 'inr' and c == 'eur' else print(a * 0.010) if b == 'eur' and c == 'inr' else print(a * 20.19) if b == 'inr' and c == 'myr' else print(a * 0.050) if b == 'myr' and c == 'inr' else print(a * 0.88) if b == 'usd' and c == 'eur' else print(a * 1.14) if b == 'eur' and c == 'usd' else print(a * 4.24) if b == 'usd' and c == 'myr' else print(a * 0.24) if b == 'myr' and c == 'usd' else print(a * 4.79) if b == 'eur' and c == 'myr' else print(a * 0.21) if b == 'myr' and c == 'eur' else None

print("THIS CONVERTER CAN CONVERT THE FOLLOWING CURRENCIES [INR,USD,EUR,MYR]")
g=['inr','usd','eur','myr']
first = input("From Currency:").lower()
second = input("To Currency:").lower()
if(first not in g and second not in g):
    print("The given input is \"INVALID\" kindly check for any typo")
else:
    num =float(input("Enter the amount:"))
    con(num,first,second)
