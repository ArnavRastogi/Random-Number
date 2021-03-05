import random
num = int(input("Enter a number: "))
range = int(input("Enter the range till the number you want to guess : "))
answer = int(range*random.random())+1
guess = 0
score = 0
print(num*10)
while guess != answer:
    guess = int(input("Guess a number : "))
    too = ""
    size = ""

    if guess > answer:
        dif = guess - answer
        size = "large"
    else:
        dif = answer - guess
        size = "small"

    if guess > 0:
        if dif >= int(range / 10):
            too = "too "
        if guess != answer:
            print("The number is", too + size)

    else:
        print("Please enter a positive integer")
        score -= 1
    score += 1

else:
    s = ""
    if score > 1:
        s = "s"
    print("\nCongratulations, you won!\nYou have completed the game in", score, "turn"+s+".")
