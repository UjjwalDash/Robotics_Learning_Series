from random import randint 
                         
def game():
    c=0
    score=20
    turns=10
    for i in range(1,turns+1):
        correct_digit=0
        Correct=[]
        wrong_pos=0
        num=str(randint(1000,9999))
        guess=input("Guess a 4 Digit Number:")
        if num==guess:
            score+=5
            print("You Won")
            print("Your Score is:",score)
            print("-"*80)
            c=1
            break
        else:
            score-=2
            for j in range(0,len(num)):
                for k in range(0,len(guess)):
                    if num[j]==guess[k]:
                        correct_digit+=1
                        if j==k:
                            Correct.append(int(guess[k]))
                        else:
                            wrong_pos+=1
            print("%d digits :%s guessed correctly. %d in correct position."%(correct_digit,Correct,len(Correct)))
            if wrong_pos>0:
                print("%d in wrong position"%(wrong_pos))
            print("Turns remaining-",turns-i)
            print("-"*80)
    if c==1 or i==turns:
        option=input("Do you want to play again?(y/n):").lower()
        print("-"*80)
        if option=='y':
            game()
        else:
            i=turns
game()
            

            

        
        
        
        
    


