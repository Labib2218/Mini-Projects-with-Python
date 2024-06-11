import time
s_time = time.time()
print("\n..........Welcome to my QUIZ Game..........")
print("WARNING: Please read the question carefully and give the right answer.",'\n')


#playing decision take
playing = input("Do you want to play this game? ")
if playing.lower() == "yes":
    print("\nLet's Go.")
    print("We ask you only 10 questions",'\n')
else:
    print("You must try this game at lest once.BTW,Thanks for your valuable time.")
    quit()

#question and answer checking
print("-----Question starts from here-----\n")
score = 0
answer = input("1.How many continents are there on Earth? ")
if answer.lower() == "seven":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("2.What planet is known as the Red Planet? ")
if answer.lower() == "mars":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("3.Which desert is the largest in the world? ")
if answer.lower() == "the sahara desert" or answer.lower() == "sahara" or answer.lower() == "sahara desert":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("4.What country has the most natural lakes? ")
if answer.lower() == "canada":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("5.Who played Jack Dawson in the movie 'Titanic'? ")
if answer.lower() == "leonardo dicaprio" or answer.lower() == "leonardo":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("6.What year did World War I begin? ")
if answer.lower() == "1914":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("7.What is the powerhouse of the cell? ")
if answer.lower() == "mitochondrion" or answer.lower() == "mitochondria":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("8.Which pop star is known as the 'Queen of Pop'? ")
if answer.lower() == "madonna":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("9.What is the capital city of France? ")
if answer.lower() == "paris":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")

answer = input("10.What country hosted the 2016 Summer Olympics? ")
if answer.lower() == "brazil":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")


#score printing section
print(f"Your total score is: {score} out of 10")
print("You got " + str(score/10 * 100)+"% answer correct.\n")
answer_script = ['Seven','Mars','The Sahara Desert','Canada','Leonardo DiCaprio','1914','The Mitochondrion or Mitochondria',
                 'Paris','Madonna','Brazil']

#answer printing section
x = input("Do you want to see all correct answer? ")
if x.lower() == "yes":
    print("\nCorrect Answers")
    for i,j in enumerate(answer_script, start=1):
        print(f'{i}.{j}')
else:
    print("\nThank You for your most valuable time.")
print("\nThank You for your most valuable time.")

e_time = time.time()
print(f"\nTotal time you spend here is: {e_time-s_time} seconds")
