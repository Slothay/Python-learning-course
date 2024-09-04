print(int("123") + int(234))

print(int(23.23))

#input -> str josta len -> int ---> Tarvitsee muuttaa vielä takaisin string-muotoon.
# print("Number of letters in your name: " + str(len(input("Enter your name"))))

name = input("Enter your name")
length = len(name)

print(f"Number of letters in your name: {length}")
