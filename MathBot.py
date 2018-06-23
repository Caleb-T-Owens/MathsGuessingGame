import random
print ('If you have played before Type 1 if you havent Type 2')
PlayedBefore = int(input ('>>>'))
if PlayedBefore == 1:
    print ('Do you remember your previous score? Yes (1) No (2)')
    PreviousScore = int(input ('>>>'))
    if PreviousScore == 1:
        print ('What was your sore?')
        Score = int(input ('>>>'))
    if PreviousScore == 2:
        Score = 0
if PlayedBefore == 2:
    Score = 0
print ('Would you like to set a custom score deduction rate? Yes (1) No (2)')
CScoreRQ = int(input ('>>> '))
if CScoreRQ == 1:
    print ('What would you like that rate to be?')
    CScoreR = int(input ('>>> '))
if CScoreRQ == 2:
    CScoreR = 1
print ('Would you like to set a custom score increace rate? Yes (1) No (2)')
CscoreIQ = int(input ('>>> '))
if CscoreIQ == 1:
    print ('What would you like that score to be?')
    CScoreI = int(input ('>>> '))
if CscoreIQ == 2:
    CScoreI = 1
print ('What mode do you want: Easy (1) Medium (2) Hard (3) Custom (4)')
Mode = input ('>>> ')
if int(Mode) == 1:
    A1 = 1
    A2 = 12
    B1 = 1
    B2 = 12
if int(Mode) == 2:
    A1 = 1
    A2 = 100
    B1 = 1
    B2 = 100
if int(Mode) == 3:
    A1 = 1
    A2 = 1000
    B1 = 1
    B2 = 1000
if int(Mode) == 4:
    A1 = int(input ('What would you like the first number to be? (_ to B * C to D)'))
    A2 = int(input ('What would you like the second number to be? (A to _ * C to D)'))
    B1 = int(input ('What would you like the third number to be? (A to B * _ to D)'))
    B2 = int(input ('What would you like the fourth number to be? (A to B * C to _)'))
while True:
        Var1 = random.randint(A1, A2)
        Var2 = random.randint(B1, B2)
        print ('Your score is : ' + str(Score))
        print (' ')
        print ('What is ' + str(Var1) + ' * ' + str(Var2) + ' ?' )
        print (' ')
        Ans = input ('>>> ')
        print (' ')
        Lock = 1
        if int(Ans) == Var1 * Var2:
            print ('Good Job!')
            print (' ')
            Score = Score + CScoreI
        else:
            while Lock == 1:
                if int(Ans) > Var1 * Var2:
                    Score = Score - CScoreR
                    print ('The correct awnser is lower, guess again!')
                    print (' ')
                    print ('Your score is : ' + str(Score))
                    print (' ')
                    Ans = input ('>>> ')
                    print (' ')
                if int(Ans) < Var1 * Var2:
                    Score = Score - CScoreR
                    print ('The correct awnser is higher, guess again!')
                    print (' ')
                    print ('Your score is : ' + str(Score))
                    print (' ')
                    Ans = input ('>>> ')
                    print (' ')
                if int(Ans) == Var1 * Var2:
                    print ('Well Done! You got it correct!')
                    print (' ')
                    Score = Score + CScoreI
                    Lock = 0