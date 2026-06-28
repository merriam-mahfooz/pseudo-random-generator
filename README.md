# **Linear Congruential Generator (LCG) in Python**

## Overview

This project is a simple Python implementation of the Linear Congruential Generator (LCG). It is one of the oldest and well-known algorithms to generate pseudo-random numbers.

The project was created as part of my Python learning journey.
I got this idea after I learned about the generation of pseudo-random numbers in Mathematics.

## Formula

The Linear Congruential Generator uses the following formula:

X(n+1) = (a*X(n)+c) mod m

Where:

X(n) = Current number(seed), 
a = Multiplier, 
c = Increment, 
m = Modulus, 
X(n+1) = Next generated number

## How it works?

1. Start with an initial seed value.
2. Multiply the seed by the multiplier.
3. Add the increment.
4. Take the remainder after dividing by the modulus.
5. The result becomes the next number in the sequence.
6. Repeat the process to generate more numbers. 

### Example Input:
Multiplier (a): 5


Increment (c): 3


Modulus (m): 16


Seed(X(0)): 7


Number of random numbers: 10

**Output**
```
Enter the multiplier: 5
Enter the increment: 3
Enter the modulus: 16
Enter the seed: 7
Enter the number of random numbers to generate: 10
Generated random numbers:
6 1 8 11 10 5 12 15 14 9 
```

## How to Run

1. Clone this repository.
2. Open the project in your preferred Python IDE or editor.
3. Run the Python file.
4. Enter the required values when prompted.

## Requirements
- Python 3.x
- No external libraries required.

## Project Structure
```
pseudo-random-generator
|
|--lcg.py
|--README.md
```
## Author
**Merriam Mahfooz**  
Created as a part of learning Python.


