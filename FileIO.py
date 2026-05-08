# Part 1 - write and read a file
with open("data.txt", "w") as f:
    f.write("Giri\n")
    f.write("Ravi\n")
    f.write("Mahesh\n")

with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())

# Part 2 - error handling
try:
    with open("doesnotexist.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("file not found")
finally:
    print("done")

# Part 3 - custom exception
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Cannot withdraw {amount}, balance is {balance}")
    return balance - amount

try:
    result = withdraw(1000, 5000)
except InsufficientFundsError as e:
    print(f"Error: {e}")