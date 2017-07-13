import random

if __name__ == "__main__":
    x = random.randrange(0, 10)
    name = input('What is your name?\n')

    names = ("", "Joe", "Fred", "Barbara")

    print(names)

    for njasfksd in names:
        print(njasfksd)

    if x in range(1,4):
        print("your name might be {name} but I will call you {other}".format(
            name=name,
            other=names[x]
        ))
    else:
        print('Hi, %s.' % name, x)
