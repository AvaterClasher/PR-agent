import random

a = random.randint(1, 12)
b = random.randint(1, 12)

for i in range(10):
    question = "What is " + a + " x " + b + "? "
    answer = int(input(question))
    if answer = a * b:
        print("Well done!")
    else:
        print("No.")
