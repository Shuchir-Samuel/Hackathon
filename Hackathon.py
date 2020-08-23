import random
import time


level = ''
ans = ''

#The list of randomly generated integers for elementary level
easy_random_ints = []
#All operations used
operations = [" divided by ", " added to ", " multiplied by ", " subtracted from "]
#Dictionary of easy questions with the key as the question and the value as the answer
easy_questions = {}
currentques = ''
correct = 0
wrong = 0

#Defining timer
def timer(): 

  now = time.localtime(time.time()) 

  return now[5]

#Adding the random numbers to the list
def add_easy_ints():
    for x in range(40):
        easy_random_ints.append(random.randint(1, 2000))
#Running the adding function
add_easy_ints()


#Making a list of randomly generated numbers used to get a random operation
operation_random_nums = []
for x in range(40):
  operation_random_nums.append(random.randint(0, len(operations)-1))
  

#Converting text operations to operations usable by Python
def operation_convert(operation, a, b):
  if operation == " divided by ":
    return round(a/b, 3)
  elif operation == " added to ":
    return a+b
  elif operation == " multiplied by ":
    return a*b
  elif operation == " subtracted from ":
    return b-a

#Add questions to the dictionary
for x in range(15):
  easy_questions[str(easy_random_ints[x]) +
              str(operations[operation_random_nums[x]]) +
              str(easy_random_ints[x+1])
              ] = operation_convert(operations[operation_random_nums[x]], easy_random_ints[x], easy_random_ints[x+1])


#Checks if the user's answer is correct
def check_ans():
  global ans
  global currentques
  ans = input("Enter your answer: ")
  while ans == " ": 
    print("Please enter a numerical answer.")
    ans = input("Enter your answer: ") 
  while ans == "-": 
    print("Please enter a numerical answer.")
    ans = input("Enter your answer: ")    
  ans2 = float(ans)
  if ans2 == easy_questions[currentques]:
      return True      
  else:
      return False    

  
    

#What to do for Math
def Math():
    global currentques
    global level
    global correct
    global wrong
    #print("Problems (round all division answers to the nearest thousandth: ")
    #Do the following for the next ten times
    for x in range(10):
      #Set the current question variable
      currentques = str(easy_random_ints[x]) + str(operations[operation_random_nums[x]]) + str(easy_random_ints[x+1])
      print(currentques)
      #After user enters answer:
      if check_ans():
        print("Your answer was correct.")
        print()
        correct += 1
      else:
        print("Your answer didn't match ours. Try again on the next one - maybe you'll get the next one!\n The correct answer was: "+ str(easy_questions[currentques]))
        print()
        wrong += 1
    
    print("You got " + str(correct) + " question(s) right and " + str(wrong) + " question(s) wrong.")
    


print()
print()


print("Welcome to Airliner Math Programs! This program will help you improve the speed and accuracy of your computation skills. Please read the directions carefully.")
print("Please round all division answers to the nearest thousand answer. If you answer incorrectly, you will be prompted to enter a second answer. If you enter another incorrect answer, the correct answer will be given.")
print()


Math() 
