# This program says hello and asks for my name.
import time

print('Hello, world!')
print('What is your name?')  # ask for the user's name

userName = input()
print('It\'s good to meet you, ' + userName + '!')
time.sleep(1)

print('Did you know that the length of your name is ' + str(len(userName)) + ' characters long?')
time.sleep(2)

print('Of course you did, you look like a smart person.')
time.sleep(2)

print('Now, tell me... What is your age?')  # ask for the user's age
userAge = input()

while not userAge.isnumeric():  # validate that the user enters only numbers
    print('Don\'t be funny. Please enter a number!')
    userAge = input()

print('In one year from now, you will be precisely...')
time.sleep(2)

print('...' + str(int(userAge) + 1) + ' years old!')

"""Practice Questions

1. Which of the following are operators, and which are values?

*  operator
'hello'  value
-88.8  value
-  operator
/  operator
+  operator
5  value

2. Which of the following is a variable, and which is a string?

spam  variable
'spam'  string

3. Name three data types.  
integer, float, string

4. What is an expression made up of? What do all expressions do?  
the expression is made up of values and operators; all expressions evaluate to a single final value

5. This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?
a statement is a command to the computer, while an expression is a combination of values and operations

6. What does the variable bacon contain after the following code runs?

bacon = 20
bacon + 1

20, because it was not assigned the value of bacon + 1

7. What should the following two expressions evaluate to?

'spam' + 'spamspam'  'spamspamspam'
'spam' * 3  'spamspamspam'

8. Why is eggs a valid variable name while 100 is invalid?  
variable names cannot begin with numbers

9. What three functions can be used to get the integer, floating-point number, or string version of a value?
int()
float()
str()

10. Why does this expression cause an error? How can you fix it?

'I have eaten ' + 99 + ' burritos.'

it causes an error because it concatenates two different data types

Correct: 'I have eaten ' + str(99) + ' burritos.'

"""