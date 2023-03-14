import random

HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for toss in range(TOSSES):
        if random.randint(1,2) == 1:
            print("Heads")
        else:
            print("Tails")

main()