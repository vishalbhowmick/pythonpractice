import random
def fn():
    a = []
    with open('word1', 'r') as f:
        line = f.readline().strip()
        while line:
            a.append(line)
            line = f.readline().strip()
    b = random.choice(a)
    print(b)
    print("The letter has ", len(b), "alphabets", "\n>>GUESS")
    c = 0
    f = 0
    g = input()
    while f != len(b) - 1:
        if g == b[f]:
            print('RIGHT GUESS')
            f += 1
            g = input(">>GUESS\n")
        elif g != b[f]:
            print('wrong,try again', '\n>>GUESS')
            c += 1
            g = input("\n")

    print("you take total ", c, "TRY to guess the word")
    print(b)


fn()

l = int(input("Press 0 to play again or 1 no. to exit"))
while l != 1:
    if l == 0:
        fn()
        l = int(input("Press 0 to play again or 1 to exit"))
    else:
        break
print("thanks for playing")