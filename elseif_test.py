age = int(input())
balance = 9000

if 7 <= age <= 12:
    fare = 650
elif 13 <= age <= 18:
    fare = 1050
elif age >= 19:
    fare = 1250

balance = balance - fare

print(balance)
