# main()
name = input("What is your name?")
print(f"Hello {name}.")
hex = 0
decimal = 0
if var.startswith("0x"):
    print("This is a hex.")
    hex = 1
else:
    print("This is a decimal")
    decimal = 1
if hex == 1:
    binary_value = bin(int(var, 16))
    print(f"{binary_value}")
if decimal == 1:
    binary_value = bin(int(var, 10))
    print(f"{binary_value}")
def main():
    name = input("What is your name?")
    print(f"Hello {name}.")
    var = input("Enter your input")
def parse_input(input):
    hex = 0
    decimal = 0
    if var.startswith("0x"):
        print("This is a hex.")
        hex = 1
    else:
         print("This is a decimal")
         decimal = 1
def convert_to_binary(type):
    if hex == 1:
        binary_value = bin(int(var, 16))
        print(f"{binary_value}")
    if decimal == 1:
        binary_value = bin(int(var, 10))
        print(f"{binary_value}")
