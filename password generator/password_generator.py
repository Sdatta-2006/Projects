import random
import string
print("Password Generator:\n")
l=int(input("Enter the length of the password you want to generate: "))
ch=string.digits+string.ascii_lowercase+string.ascii_uppercase+string.punctuation
p=""
for i in range(l):
    p=p+random.choice(ch)

print("The generated password: "+p)