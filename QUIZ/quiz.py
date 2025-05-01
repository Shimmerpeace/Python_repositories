playing = input("Are you ready to play? ")

if playing.lower() != "yes":
    quit()
print("Ready! Let's play 😊 !")
score = 0

question1 = input("What is the highest mountain peak in the world? ")
if question1.lower() == "mount everest":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

question2 = input("Which ocean is the largest of the world's five oceans? ").lower()
if question2 == "pacific ocean":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

question3 = input("What is the process by which plants release water vapor into the air? ")
if question3.lower() == "transpiration":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

question4 = input("What is the term for a community of living and non-living things that interact with each other? ")
if question4.lower() == "ecosystem":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

question5 = input("What is the world's largest waterfall, by volume of water? ")
if question5.lower() == "victoria falls":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / 5) * 100) + "%.")
