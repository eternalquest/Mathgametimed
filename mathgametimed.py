import random
import time
#stores constant values
OPERATORS= ["+","-","*"]
MIN_OPERAND=3
MAX_OPERAND=12
TOTAL_PROBLEMS=10
#function to generate math problems
def generate_problem():
    left=random.randint(MIN_OPERAND,MAX_OPERAND)
    right=random.randint(MIN_OPERAND,MAX_OPERAND)
    operators=random.choice(OPERATORS)

    expr= str(left) + ""+ operators +""+str(right)
    answer= eval(expr)
  
    return expr,answer
#var to stores wrong attempts
wrong=0

input("press enter to start!")
print("----------------------")
start_time=time.time()


for i in range(TOTAL_PROBLEMS):
    expr,answer=generate_problem()
    while True:
        guess=input("Problem #" + str(i+1)+":"+expr+"=")
        if guess==str(answer):
            break
        wrong +=1
end_time=time.time()
total_time=round(end_time-start_time,2) #stores and rounds off total time taken

print("----------------------")

print("wrong answers:",wrong)#prints wrong answers
print("Nice work! you finished in: ",total_time,"seconds!") #prints total time taken