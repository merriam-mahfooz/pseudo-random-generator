def lcg (multiplier, increment, modulus, seed,count):
    current=seed
    
    for i in range(count):
        next = (multiplier * current + increment) % modulus
        print(next, end=" ")
        current=next
    
multiplier = int(input("Enter the multiplier: "))
increment = int(input("Enter the increment: "))
modulus = int(input("Enter the modulus: "))
seed = int(input("Enter the seed: "))
count = int(input("Enter the number of random numbers to generate: "))
print("Generated random numbers:")
lcg(multiplier, increment, modulus, seed, count)
