#python quiz game

questions = ("what is capital of india?",
             "What is 99+1 value?",
             "who is prime minister of india?",
             "when was 1st world war is happened?")
options = (("A.Amaravati", "B.Amritsar", "C.Pondicherry", "D.New Delhi"),
           ("A.200", "B.101", "C.100", "D.91"),
           ("A.Narendra Modi", "B.DroupadiMurmu", "C.Manmohansingh", "D.A.P.J Abdul kalam"),
           ("A.2000-2007", "B.1914-1919", "C.1890-1897", "D.1999-2004"))
answers = ("D","C","A","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): " ).upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT:")
        print(f"{answers[question_num]} is the correct answer")
question_num += 1

print("--------------------")
print("       RESULTS      ")
print("--------------------")

print("answers: ",end = "")
for answer in answers:
    print(answer, end = " ")
print()

print("guesses: ",end = "")
for guess in guesses:
    print(guess, end = " ")
print()

score = int(score / len(questions) * 100)
print("Your score is : {score} %")