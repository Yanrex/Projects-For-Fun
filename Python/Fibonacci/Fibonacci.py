import sys

print("Welcome!\nThis program prints you the first N elements of the Fibonacci sequence.")
print("If you'd like to exit the program just type in anything that is not an integer.")
while True:
    number = input("Enter a positive integer: ")
    try:
        N = int(number) + 1
        if N <= 0:
            print("Input must be a positive integer.")
            continue
    except ValueError:
        print("Goodbye.")
        input("Press any key to exit...")
        break
    print(str(1) + '. ' + str(0))
    i = 0
    j = 1
    for n in range(2, N):
        print(str(n) + '. ' + str(j))
        help = i
        i = j
        j = help + j