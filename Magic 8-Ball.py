# The purpose of this mini project is to model how a Magic 8-Ball works when you ask it a question. 
# Try editing the code to include what would happen if John didn't ask a question.

name = "John"
question = "Will I become fluent in Spanish?"
answer = ""

if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)

import random

random_number = random.randint(1, 11)
# print(random_number)

if random_number  == 1:
  print("Yes - definitely.")
elif random_number == 2:
  print("It is decidedly so.")
elif random_number == 3:
  print("Without a doubt.")
elif random_number == 4:
  print("Reply hazy, try again.")
elif random_number == 5:
  print("Ask again later.")
elif random_number == 6:
  print("Better not tell you now.")
elif random_number == 7:
  print("My sources say no.")
elif random_number == 8:
  print("Outlook not so good.")
elif random_number == 9:
  print("Very doubtful.")  
elif random_number == 10:
  print("That's impossible.")
elif random_number == 11:
  print("Never in a million years.") 
else:
  answer = "Error"