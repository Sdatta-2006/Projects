import random
b=int(input("Enter the lower limit of the range: "))
c=int(input("Enter the upper limit of the range: "))
n=random.randint(b,c)
g=0
a=0
print(f"Welcome to the number guessing game: \nGuess a number from {b} to {c}")
while g!=n:
    g=int(input("Enter the number you guessed: "))
    a=a+1
    if g>n:
        print("Your number is too big!")
    elif g<n:
        print("Your number is too small!")
    else:
        print(f"Congratulation! You have guessed the correct number in {a} attempts!")