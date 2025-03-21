score = int(input("Whats your score"))
if 90 <= score <= 100:
   print("Your possition is excellent")
elif 80 <= score < 90:
   print("very good")
elif 70 <= score < 80:
   print ("good")
elif 60 <= score < 70:
   print ("satisfactory")
elif 50 <= score < 60:
   print ("needs improvement")
elif 0 <= score < 50:
   print("fail")
else:
   print ("invalid score, input a number between 0 to 100")