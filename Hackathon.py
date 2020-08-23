import random
import time
#import pgzrun
#import pgzero
#import pygame



timer = 5
timerdone = False

      
###########################################################
#TRY NOT TO EDIT ANYTHING. I HAVE A NICE TIMER IN PLACE, I JUST NEED TO TWEAK SOME STUFF FOR IT TO WORK>
###########################################################


level = ''
ans = ''
#TO REMOVE: The list of random integers for the middle level
#TO REMOVE: middle_random_ints = []
#The list of randomly generated integers for elementary level
easy_random_ints = []
#All operations used
operations = [" divided by ", " added to ", " multiplied by ", " subtracted from "]
#Dictionary of easy questions with the key as the question and the value as the answer
easy_questions = {}
currentques = ''
score = 0


#Defining timer
def timer(): 

  now = time.localtime(time.time()) 

  return now[5]

#Adding the random numbers to the list
def add_easy_ints():
    for x in range(11):
        easy_random_ints.append(random.randint(1, 20))
#Running the adding function
add_easy_ints()

#Function to add random integers to list
#TO REMOVE: def add_middle_ints():
#  for x in range(6):
#    middle_random_ints.append(random.randint(1, 10000))


#Making a list of randomly generated numbers used to get a random operation
operation_random_nums = []
for x in range(11):
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
for x in range(10):
  easy_questions[str(easy_random_ints[x]) +
              str(operations[operation_random_nums[x]]) +
              str(easy_random_ints[x+1])
              ] = operation_convert(operations[operation_random_nums[x]], easy_random_ints[x], easy_random_ints[x+1])


#Checks if the user's answer is correct
def check_ans():
  global ans
  global currentques
  ans = float(input("Enter your answer: "))
  if ans == easy_questions[currentques]:
    return True
  else:
    return False

#What to do when user picks Math
def Math():
    global currentques
    global level
    global score
    print("Problems (round all division answers to the nearest thousandth: ")
    #run = input("Start? ")  
    #while run == "yes": 
      #current_sec = 0
      #current_sec = timer()
      #if current_sec == 10:
        #print("GAME OVER")
    #Do the following for the next five times
    for x in range(10):
      #Set the current question variable
      currentques = str(easy_random_ints[x]) + str(operations[operation_random_nums[x]]) + str(easy_random_ints[x+1])
      print(currentques)
      time.sleep(1)
      #After user enters answer
      if check_ans():
        print("Your answer was correct.")
        print()
        score += 1
      elif not check_ans():
        print("Your answer didn't match ours. Try again on the next one! Maybe you'll get the next one!\n The correct answer was: "+ str(easy_questions[currentques]))
        print()
        score -= 1
    print("You got " + str(score) + " right.")
      


print()
print()

print("Welcome to Airliner Math Programs! This program will help you improve the speed and accuracy of your computation skills. Please read the directions carefully.")
print("Please round all division answers to the nearest whole number for the math section(s). Note that if you enter a wrong answer, you will be prompted to enter a second answer. If you enter another incorrect answer, the correct answer will be given.")
print()

time.sleep(1)

Math()

