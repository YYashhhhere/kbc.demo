questions = ['1. What is the correct way to define a tuple with one element?',
             '2. Are tuples mutable in Python?',
             '3. Which of the following is used to define a function in Python?',
             '4. What is the output of: print(2 ** 3)?',
             '5. What does the input() function do?']

options = [['A. t = (5)','B. t = [5]','C. t = (5,)','D. t = (5,5)'],
           ['A. NO','B. Yes','C. Depends on the version','D. If it contain lists'],
           ['A. function','B. define','C. def','D. func'],
           ['A. 6','B. 8','C. 4','D. 10'],
           ['A. shows output','B. Exits the program','C. Converts strings to integers','D. Reads a line from the user ']]

answers = ['C','A','C','B','D']

price = [1000,5000,10000,15000,20000]
money = 0
print('\nWelcome to the game 😊')
print('Your game has started')

for i in range(0,len(questions)):
  print(f'\nquestion for {price[i]} rs✨')
  print(questions[i])

  for j in options[i]:
    print(j)

  askValue = input('choose option between A-D💭- ').upper()

  if(askValue == answers[i]):
    print(f'\nYour answer is correct 🎉')
    money += price[i]
    print(f'You won {price[i]} rs')
    print(f'Your total amount is {money} rs')
  else:
    print('\nOps!😬, Your answer is incorrect, your game is over')
    print(f'\nthe correct answer was {answers[i]}')
    print(f'Your final amount is {money} rs')
    break
