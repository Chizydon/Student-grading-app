Grading App
A simple python app made to determine a student's position based on their score. if the score is bellow 50, it will tell him that you fail.

Ensure you have Python installed on your system. You can check by running: python --version If Python is not installed, download and install it from python.org. Installation

The program will prompts the user to enter a score of number.

it will them bring it to position based on the score

Example usage:

grade.py

enter score, if score is bellow 49
result : fail
if 50 to 60:
result: needs improvement; till
if 90 to 100
result: Excellent

Code Example
def grade():

score = int(input("Whats your score"))
if 90 <= score <= 100:
   print("Your possition is excellent")
elif 80 <= score < 89:
   print("very good")
elif 70 <= score < 79:
   print ("good")
elif 60 <= score < 69:
   print ("satisfactory")
elif 50 <= score < 59:
   print ("needs improvement")
elif 0 <= score < 49:
   print("fail")
else:
   print ("invalid score, input a number between 0 to 100")


Contributing

Feel free to contribute by submitting issues or pu;; requests.
   
    
